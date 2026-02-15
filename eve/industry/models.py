from django.db import models

from eve.industry.mixins import PublishedMixin, CreatedAtMixin


# Create your models here.

class Categories(PublishedMixin, CreatedAtMixin):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class Groups(PublishedMixin, CreatedAtMixin):
    group_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class MarketGroups(CreatedAtMixin):
    market_group_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()



