# news/views/news.py
from rest_framework import viewsets, permissions, filters
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
        "status",
    ]

    ordering_fields = [
        "order",
        "created_at",
    ]

    def perform_destroy(self, instance):
        instance.soft_delete()
