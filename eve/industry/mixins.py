from django.db import models


class CreatedAtMixin(models.Model):
    created_at = models.DateField(auto_now=True, blank=True, null=True)
    class Meta:
        abstract = True

class CreatedAtDateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        abstract = True



class PublishedMixin(models.Model):
    published = models.BooleanField(default=False)
    class Meta:
        abstract = True

