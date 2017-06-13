from django.conf.urls import url
import views


urlpatterns = [
    url(r'createRegion/$', views.RegionListCreateView.as_view(), name='create-regions'),
    url(r'listRegions/$', views.RegionListCreateView.as_view(), name='list-regions'),
    url(r'getRegion/(?P<pk>[0-9]+)/$', views.RegionDetailModifyView.as_view(), name='get-region-detail'),
    url(r'updateRegion/(?P<pk>[0-9]+)/$', views.RegionDetailModifyView.as_view(), name='update-region'),
    url(r'deleteRegion/(?P<pk>[0-9]+)/$', views.RegionDetailModifyView.as_view(), name='delete-region'),

    url(r'createInstance/$', views.InstanceListCreateView.as_view(), name='create-instance'),
    url(r'listInstance/$', views.InstanceListCreateView.as_view(), name='list-instance'),
    url(r'getInstance/(?P<pk>[0-9]+)/$', views.InstanceDetailModifyView.as_view(), name='get-instance-detail'),
    url(r'updateInstance/(?P<pk>[0-9]+)/$', views.InstanceDetailModifyView.as_view(), name='update-instance'),
    url(r'deleteInstance/(?P<pk>[0-9]+)/$', views.InstanceDetailModifyView.as_view(), name='delete-instance'),

    url(r'createSizePrice/$', views.SizePriceListCreateView.as_view(), name='create-instance'),
    url(r'listSizePrice/$', views.SizePriceListCreateView.as_view(), name='list-instance'),
    url(r'getSizePrice/(?P<pk>[0-9]+)/$', views.SizePriceDetailModifyView.as_view(), name='get-instance-detail'),
    url(r'updateSizePrice/(?P<pk>[0-9]+)/$', views.SizePriceDetailModifyView.as_view(), name='update-instance'),
    url(r'deleteSizePrice/(?P<pk>[0-9]+)/$', views.SizePriceDetailModifyView.as_view(), name='delete-instance'),
]
