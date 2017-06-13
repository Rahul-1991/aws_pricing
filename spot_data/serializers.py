from rest_framework import serializers
from .models import RegionModel, InstanceModel, SizePriceModel


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegionModel
        fields = ('id', 'region_name')


class InstanceSerializer(serializers.ModelSerializer):
    region_id = serializers.SlugRelatedField(slug_field='instance_type', queryset=RegionModel.objects.all())

    class Meta:
        model = InstanceModel
        fields = ('id', 'region_id', 'instance_type')


class SizePriceSerializer(serializers.ModelSerializer):
    instance_id = serializers.SlugRelatedField(slug_field='size', queryset=InstanceModel.objects.all())

    class Meta:
        model = SizePriceModel
        fields = ('id', 'instance_id', 'size', 'price')

