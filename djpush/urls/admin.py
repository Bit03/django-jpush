from django.urls import path

from djpush.views.admin_api import (
    AdminCreateAPIView,
    AdminDeleteAPIView,
)

urlpatterns = [
    path("create/", AdminCreateAPIView.as_view(), name="create"),
    path("delete/", AdminDeleteAPIView.as_view(), name="delete"),
]
