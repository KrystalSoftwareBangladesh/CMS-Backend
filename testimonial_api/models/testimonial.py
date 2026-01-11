from django.db import models

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel


class Testimonial(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(
        max_length=100,
        help_text="Name of the person giving the testimonial"
    )
    designation = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Designation or role (e.g. CEO, Client)"
    )
    company = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text="Company or organization name"
    )
    message = models.TextField(
        help_text="Testimonial message/content"
    )
    avatar = models.ImageField(
        upload_to="testimonials/avatars/",
        null=True,
        blank=True
    )
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Rating out of 5"
    )
    is_featured = models.BooleanField(
        default=False,
        db_index=True
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.company or 'Individual'}"
