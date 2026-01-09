from rest_framework import serializers

from faq_api.models import FAQ
# from category_api.models import Category


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = [
            "id",
            "question",
            "answer",
            "category",
            "order",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    # VALIDATIONS
    # def validate_category(self, category: Category):
    #     """
    #     Ensure FAQ is only assigned to FAQ categories.
    #     """
    #     if category.content_type != Category.ContentType.FAQ:
    #         raise serializers.ValidationError(
    #             "Only categories with content_type='faq' can be assigned to FAQs."  # noqa
    #         )
    #     return category
