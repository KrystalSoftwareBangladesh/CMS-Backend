from rest_framework import serializers

from team_api.models import TeamMemberSocial


class TeamMemberSocialSerializer(serializers.ModelSerializer):
    platform_name = serializers.CharField(
        source="platform.name",
        read_only=True
    )
    platform_icon = serializers.ImageField(
        source="platform.icon",
        read_only=True
    )

    class Meta:
        model = TeamMemberSocial
        fields = (
            "platform",
            "platform_name",
            "platform_icon",
            "profile_url",
            "order",
        )
