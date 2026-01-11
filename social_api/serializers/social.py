from rest_framework import serializers

from social_api.models import SocialPlatform


class SocialPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = [
            "id",
            "name",
            "key",
            "icon",
            "icon_svg",
            "base_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_key(self, value):
        return value.lower().strip()

    def validate_icon_svg(self, value):
        if value and not value.strip().startswith("<svg"):
            raise serializers.ValidationError(
                "icon_svg must be a valid SVG markup."
            )
        return value
