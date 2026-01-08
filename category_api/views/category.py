# category_api/views/category.py
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from category_api.models import Category
from category_api.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(
        deleted_at__isnull=True
    )

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        # "content_type",
        # "country_code",
        "parent",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = ["name"]

    # ---------------------------
    # QUERY OPTIMIZATION
    # ---------------------------
    def get_queryset(self):
        qs = super().get_queryset()

        # Optional: restrict by content_type query param
        # content_type = self.request.query_params.get("content_type")
        # if content_type:
        #     qs = qs.filter(content_type=content_type)

        return qs
