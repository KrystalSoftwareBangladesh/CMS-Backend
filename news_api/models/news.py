# news_api/models/news.py
from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel

from category_api.models import Category


class News(TimeStampedModel, SoftDeleteModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="news"
    )
    excerpt = models.CharField(
        max_length=500,
        help_text="Short description shown in news card"
    )
    content = models.TextField(
        help_text="Full news content"
    )
    cover_image = models.ImageField(
        upload_to="news/covers/"
    )
    author_name = models.CharField(max_length=100)
    read_time = models.PositiveSmallIntegerField(
        help_text="Estimated read time in minutes"
    )

    is_featured = models.BooleanField(
        default=False,
        db_index=True
    )
    is_highlighted = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Highlighted news (multiple allowed)"
    )
    status = models.BooleanField(
        default=True,
        db_index=True,
        help_text="Frontend visibility"
    )

    order = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "News"
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_featured:
            (
                News.objects
                .filter(is_featured=True)
                .exclude(pk=self.pk)
                .update(is_featured=False)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
