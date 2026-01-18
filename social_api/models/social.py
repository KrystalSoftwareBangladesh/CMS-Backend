from django.db import models

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel


class SocialPlatform(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=50)  # Facebook, LinkedIn
    key = models.CharField(max_length=30, unique=True)  # facebook, linkedin
    icon = models.CharField(max_length=100, null=True, blank=True)
    icon_svg = models.TextField(
        null=True,
        blank=True,
        help_text="SVG path only (d attribute)"
    )
    base_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Social Platform"
        verbose_name_plural = "Social Platforms"

    def __str__(self):
        return self.name
