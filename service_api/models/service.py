# services/models.py
from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import SoftDeleteModel, TimeStampedModel


class Service(TimeStampedModel, SoftDeleteModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True
    )
    description = models.TextField(blank=True)

    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
