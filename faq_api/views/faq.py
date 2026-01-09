from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone

from faq_api.models import FAQ
from faq_api.serializers import FAQSerializer


class FAQViewSet(ModelViewSet):
    serializer_class = FAQSerializer

    queryset = FAQ.objects.filter(
        deleted_at__isnull=True
    )

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "status",
    ]

    search_fields = [
        "question",
        "answer",
    ]

    ordering_fields = [
        "order",
        "created_at",
    ]

    ordering = [
        "order",
        "created_at",
    ]

    # OPTIONAL: SOFT DELETE
    def perform_destroy(self, instance):
        instance.deleted_at = timezone.now()
        instance.save()
