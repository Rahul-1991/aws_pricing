from django.db import models


class RegionModel(models.Model):
    region_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region_name


class InstanceModel(models.Model):
    region_id = models.ForeignKey(RegionModel, related_name='instances', on_delete=models.CASCADE)
    instance_type = models.CharField(max_length=255)

    def __str__(self):
        return self.instance_type


class SizePriceModel(models.Model):
    instance_id = models.ForeignKey(InstanceModel, related_name='sizeprice', on_delete=models.CASCADE)
    size = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.size

