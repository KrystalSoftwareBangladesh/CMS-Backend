# news/serializers/news.py
from rest_framework import serializers

from news_api.models import News
from category_api.models import Category

from category_api.serializers import CategorySerializer


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = (
            "id",
            "slug",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        )
