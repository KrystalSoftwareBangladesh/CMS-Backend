from rest_framework import serializers

from team_api.models import TeamMember
from team_api.models import TeamMemberSocial

from .social_link import TeamMemberSocialSerializer


class TeamMemberSerializer(serializers.ModelSerializer):
    social_profiles = TeamMemberSocialSerializer(
        many=True,
        # read_only=True
        required=False,
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

    def create(self, validated_data):
        social_profiles_data = validated_data.pop(
            "social_profiles", []
        )

        team_member = TeamMember.objects.create(
            **validated_data
        )

        TeamMemberSocial.objects.bulk_create([
            TeamMemberSocial(
                team_member=team_member,
                **social_data
            )
            for social_data in social_profiles_data
        ])

        return team_member

    def update(self, instance, validated_data):
        social_profiles_data = validated_data.pop(
            "social_profiles", None
        )

        # update TeamMember fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # if social_profiles provided, replace them
        if social_profiles_data is not None:
            # instance.social_profiles.all().delete()

            TeamMemberSocial.objects.bulk_create([
                TeamMemberSocial(
                    team_member=instance,
                    **social_data
                )
                for social_data in social_profiles_data
            ])

        return instance
