# from django.conf.urls import url
from django.urls import path
from djpush.views.push_api import (
    AudienceAPIView,
    AllAPIView,
    NotificationAPIView,
    OptionsAPIView,
    SilentAPIView,
    SmsAPIView,
    PlatformMsgAPIView,
    ValidateAPIView,
    AliasAPIView,
)

urlpatterns = [
    path("alias/", AliasAPIView.as_view(), name="alias"),
    path("audience/", AudienceAPIView.as_view(), name="audience"),
    path("all/", AllAPIView.as_view(), name="all"),
    path("notification/", NotificationAPIView.as_view(), name="notification"),
    path("options/", OptionsAPIView.as_view(), name="options"),
    path("silent/", SilentAPIView.as_view(), name="silent"),
    path("sms/", SmsAPIView.as_view(), name="sms"),
    path("platform/", PlatformMsgAPIView.as_view(), name="platform"),
    path("validate/", ValidateAPIView.as_view(), name="validate"),
]
