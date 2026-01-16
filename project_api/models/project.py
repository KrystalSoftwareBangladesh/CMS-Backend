# projects/models/project.py
from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel

from service_api.models import Service


class Project(TimeStampedModel, SoftDeleteModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True
    )
    service = models.ForeignKey(
        Service,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="projects"
    )
    short_description = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    cover_image = models.ImageField(
        upload_to="projects/covers/"
    )
    # UI metrics
    deliveries_count = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="e.g. 25K+"
    )
    countries_count = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    on_time_rate = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="e.g. 99.8"
    )
    is_featured = models.BooleanField(default=False, db_index=True)
    status = models.BooleanField(
        default=True,
        help_text="Frontend visibility"
    )

    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        db_table = "projects"
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
