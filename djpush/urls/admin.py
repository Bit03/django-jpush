from django.urls import path

from djpush.views.admin_api import (
    AdminCreateAPIView,
    AdminDeleteAPIView,
)

urlpatterns = [
    # url(r'^$', AdminAPIView.as_view(), name='list'),
    path("create/", AdminCreateAPIView.as_view(), name="create"),
    path("delete/", AdminDeleteAPIView.as_view(), name="delete"),
]
