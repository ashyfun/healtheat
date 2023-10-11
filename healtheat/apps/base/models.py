from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlankCharField(models.CharField):

    def __init__(self, max_length=255, blank=True, null=True, *args, **kwargs):
        super().__init__(max_length=255, blank=True, null=True, *args, **kwargs)
