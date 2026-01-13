from rest_framework import serializers

from category_api.models import Category
from project_api.models import Project

from category_api.serializers import CategorySerializer


class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
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
