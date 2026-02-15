from django.db import models

from eve.industry.mixins import PublishedMixin, CreatedAtMixin, CreatedAtDateTimeMixin


# Create your models here.

class Categories(PublishedMixin, CreatedAtMixin):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class Groups(PublishedMixin, CreatedAtMixin):
    group_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=200)


class MarketGroups(CreatedAtMixin):
    market_group_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

class Types(CreatedAtDateTimeMixin, PublishedMixin):
    type_id = models.IntegerField(primary_key=True)
    group_id = models.ForeignKey(to=Groups, on_delete=models.CASCADE, related_name='types', null=True, blank=True)
    market_group_id = models.ForeignKey(to=MarketGroups, on_delete=models.CASCADE, related_name='types', null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    capacity = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    packaged_volume = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    portion_size = models.IntegerField(blank=True, null=True) # the number of units produced per manufacturing run
    graphic_id = models.IntegerField(blank=True, null=True) # tells the game engine or API which 3D model file to load to render that item in space
    icon_id = models.IntegerField(blank=True, null=True) # https://images.evetech.net/types/587/icon

