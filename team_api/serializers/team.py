from rest_framework import serializers

from team_api.models import TeamMember

from .social_link import TeamMemberSocialSerializer


class TeamMemberSerializer(serializers.ModelSerializer):
    social_profiles = TeamMemberSocialSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = TeamMember
        fields = (
            "id",
            "name",
            "slug",
            "designation",
            "short_bio",
            "bio",
            "profile_image",
            "social_profiles",
            "is_featured",
            "order",
        )
