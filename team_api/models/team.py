# team_api/models/teamp.py
from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel


class TeamMember(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        max_length=160,
        unique=True,
        blank=True,
        db_index=True
    )
    designation = models.CharField(
        max_length=150,
        help_text="e.g. CEO, Software Engineer"
    )
    short_bio = models.CharField(
        max_length=300,
        blank=True
    )
    bio = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="team/profile/",
        null=True,
        blank=True,
    )

    is_featured = models.BooleanField(
        default=False,
        db_index=True
    )
    status = models.BooleanField(
        default=True,
        help_text="Frontend visibility"
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:
        db_table = "team_members"
        ordering = ["order", "-created_at"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
