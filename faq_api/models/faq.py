from django.db import models

from CMS_Backend.core.models import TimeStampedModel, SoftDeleteModel

from category_api.models import Category


class FAQ(TimeStampedModel, SoftDeleteModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="faqs"
    )

    class Meta:
        db_table = "faqs"
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.question
