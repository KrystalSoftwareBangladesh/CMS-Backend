from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel


class OfficeLocation(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(
        max_length=150,
        help_text="e.g. Dhaka Head Office, UK Branch"
    )
    slug = models.SlugField(
        max_length=160,
        unique=True,
        blank=True,
        db_index=True
    )

    country = models.CharField(
        max_length=100,
        db_index=True,
        help_text="e.g. Bangladesh, United Kingdom"
    )
    city = models.CharField(
        max_length=100,
        blank=True
    )
    address = models.TextField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )
    email = models.EmailField(
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    is_head_office = models.BooleanField(
        default=False,
        db_index=True
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
        db_table = "office_locations"
        ordering = ["order", "country", "city"]
        verbose_name = "Office Location"
        verbose_name_plural = "Office Locations"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.country})"
