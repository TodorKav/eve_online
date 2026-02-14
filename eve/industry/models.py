from django.db import models

from eve.industry.mixins import PublishedMixin


# Create your models here.

class Categories(PublishedMixin):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
