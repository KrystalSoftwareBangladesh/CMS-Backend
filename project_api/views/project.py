# projects/views/project.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from project_api.models import Project

from project_api.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = (
        Project.objects
        .filter(is_active=True)
        .select_related("service")
    )
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "short_description",
        "service__name",
    ]

    filterset_fields = [
        "service",
        "is_featured",
        "status",
    ]

    ordering_fields = ["order", "created_at"]

    def perform_destroy(self, instance):
        instance.soft_delete()
