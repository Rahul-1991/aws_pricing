from django.db import models


class RegionModel(models.Model):
    region_name = models.CharField(max_length=255, required=True)
    created_at = models.DateTimeField(auto_now_add=True)


class InstanceModel(models.Model):
    region_id = models.ForeignKey(RegionModel, related_name='instances', on_delete=models.CASCADE)
    instance_type = models.CharField(max_length=255, required=True)


class SizePriceModel(models.Model):
    instance_id = models.ForeignKey(InstanceModel, related_name='size_price', on_delete=models.CASCADE)
    size = models.CharField(max_length=255, required=True)
    price = models.FloatField()
