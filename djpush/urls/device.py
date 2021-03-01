# from django.conf.urls import url
from django.urls import path

from djpush.views.device_api import (
    AliasAPIView,
    CtrlTagAPIView,
    DeviceAPIView,
    TagAPIView,
    TagCheckAPIView,
    UserTagAPIView,
    DeviceMobileUpdateAPIView,
)

urlpatterns = [
    path("alias/", AliasAPIView.as_view(), name="alias"),
    path("device/", DeviceAPIView.as_view(), name="device"),
    path("device/mobile/", DeviceMobileUpdateAPIView.as_view(), name="mobile"),
    path("tag/", TagAPIView.as_view(), name="tag"),
    path("tag/ctrl", CtrlTagAPIView.as_view(), name="ctrl"),
    path("tag/check/", TagCheckAPIView.as_view(), name="check"),
    path("tag/user/", UserTagAPIView.as_view(), name="user"),
]
