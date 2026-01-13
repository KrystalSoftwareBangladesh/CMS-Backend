from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from service_api.models import Service
from service_api.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_featured"]
    search_fields = ["title", "short_description"]
    ordering_fields = ["order", "created_at"]

    def perform_destroy(self, instance):
        instance.soft_delete()
