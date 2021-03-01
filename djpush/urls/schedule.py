# from django.conf.urls import url
from django.urls import path

from djpush.views.schedule_api import (
    ScheduleAPIView,
    ScheduleDeleteAPIView,
)

urlpatterns = [
    path("", ScheduleAPIView.as_view(), name="default"),
    path("delete/", ScheduleDeleteAPIView.as_view(), name="delete"),
    path("get/", ScheduleDeleteAPIView.as_view(), name="get"),
    path("list/", ScheduleDeleteAPIView.as_view(), name="list"),
]
