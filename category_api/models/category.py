# category_api/models/category.py
from django.db import models
from django.utils.text import slugify

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel


class Category(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = self._generate_unique_slug()

        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1

        qs = Category.objects.filter(
            # content_type=self.content_type,
            # country_code=self.country_code,
            parent=self.parent,
            slug=slug
        )

        while qs.exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
            qs = Category.objects.filter(
                # content_type=self.content_type,
                # country_code=self.country_code,
                parent=self.parent,
                slug=slug
            )

        return slug
