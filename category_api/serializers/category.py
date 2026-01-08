# category_api/serializers/category.py
from rest_framework import serializers

from category_api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            # "content_type",
            "parent",
            # "country_code",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    # ---------------------------
    # VALIDATIONS
    # ---------------------------

    def validate_parent(self, parent):
        """
        Parent category must match:
        - content_type
        - country_code
        """
        if not parent:
            return parent

        # content_type = self.initial_data.get("content_type")
        # country_code = self.initial_data.get("country_code")

        # if parent.content_type != content_type:
        #     raise serializers.ValidationError(
        #         "Parent category must have the same content_type."
        #     )

        # if parent.country_code != country_code:
        #     raise serializers.ValidationError(
        #         "Parent category must belong to the same country scope."
        #     )

        return parent

    def validate(self, attrs):
        """
        Prevent slug updates after creation (SEO safety).
        """
        instance = self.instance

        if instance and "slug" in attrs:
            raise serializers.ValidationError(
                {"slug": "Slug cannot be updated once created."}
            )

        return attrs
