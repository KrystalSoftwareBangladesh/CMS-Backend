# team_api/models/social_link.py
from django.db import models

from CMS_Backend.core.models import TimeStampedModel


class TeamMemberSocial(TimeStampedModel):
    team_member = models.ForeignKey(
        "team_api.TeamMember",
        on_delete=models.CASCADE,
        related_name="social_profiles"
    )
    platform = models.ForeignKey(
        "social_api.SocialPlatform",
        on_delete=models.PROTECT,
        related_name="team_members"
    )
    profile_url = models.URLField(max_length=500)

    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "team_member_socials"
        ordering = ["order"]
        unique_together = ("team_member", "platform")
        verbose_name = "Team Member Social Profile"
        verbose_name_plural = "Team Member Social Profiles"

    def __str__(self):
        return f"{self.team_member.name} - {self.platform.name}"
