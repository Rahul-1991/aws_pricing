from rest_framework import serializers
from .models import RegionModel, InstanceModel, SizePriceModel


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegionModel
        fields = '__all__'


class InstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstanceModel
        fields = '__all__'


class SizePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SizePriceModel
        fields = '__all__'

