# from django.conf.urls import url
from django.urls import path
from djpush.views.zone_api import ZoneDefaultAPIView, ZoneBJAPIView

urlpatterns = [
    path("default/", ZoneDefaultAPIView.as_view(), name="default"),
    path("bj/", ZoneBJAPIView.as_view(), name="bj"),
]
