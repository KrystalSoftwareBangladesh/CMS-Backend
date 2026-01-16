from rest_framework import serializers

from service_api.models import Service
from project_api.models import Project

from service_api.serializers import ServiceSerializer


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source="service",
        write_only=True
    )

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = (
            "id",
            "slug",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        )
