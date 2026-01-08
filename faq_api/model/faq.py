from django.db import models

from CMS_Backend.core.model import TimeStampedModel, SoftDeleteModel


class FAQ(TimeStampedModel, SoftDeleteModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
