from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import RegionModel, InstanceModel, SizePriceModel
from .serializers import RegionSerializer, InstanceSerializer, SizePriceSerializer


class RegionListCreateView(ListCreateAPIView):

    queryset = RegionModel.objects.all()
    serializer_class = RegionSerializer


class RegionDetailModifyView(RetrieveUpdateDestroyAPIView):

    queryset = RegionModel.objects.all()
    serializer_class = RegionSerializer


class InstanceListCreateView(ListCreateAPIView):

    queryset = InstanceModel.objects.all()
    serializer_class = InstanceSerializer


class InstanceDetailModifyView(RetrieveUpdateDestroyAPIView):
    queryset = InstanceModel.objects.all()
    serializer_class = InstanceSerializer


class SizePriceListCreateView(ListCreateAPIView):
    queryset = SizePriceModel.objects.all()
    serializer_class = SizePriceSerializer


class SizePriceDetailModifyView(RetrieveUpdateDestroyAPIView):
    queryset = SizePriceModel.objects.all()
    serializer_class = SizePriceSerializer
