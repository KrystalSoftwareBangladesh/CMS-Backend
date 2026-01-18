# category_api/views/category.py
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from CMS_Backend.core.permission import PublicListPermissionMixin

from category_api.models import Category
from category_api.serializers import CategorySerializer


class CategoryViewSet(PublicListPermissionMixin, viewsets.ModelViewSet):
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

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
