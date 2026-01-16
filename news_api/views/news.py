# news/views/news.py
from rest_framework import viewsets, permissions, filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from news_api.models import News
from news_api.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = (
        News.objects
        .filter(is_active=True)
        .select_related("category")
    )
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]  # lock later

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "excerpt",
        "content",
        "author_name",
        "category__name",
    ]

    filterset_fields = [
        "category",
        "is_featured",
        "is_highlighted",
        "status",
    ]

    ordering_fields = [
        "order",
        "created_at",
    ]

    def perform_destroy(self, instance):
        instance.soft_delete()

    @action(detail=False, methods=["get"], url_path="featured")
    def featured(self, request):
        featured_news = (
            self.get_queryset()
            .filter(is_featured=True)
            .first()
        )

        if not featured_news:
            return Response(
                {"detail": "No featured news found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(featured_news)
        return Response(serializer.data)
