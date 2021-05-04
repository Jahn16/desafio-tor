from django.contrib import admin
from django.urls import path,include

from .views import IpListAPIView, ExternalSourceIpOnlyListAPIView, InternalSourceIpOnlyListAPIView, IpCreateAPIView

app_name = "api-ips"

urlpatterns = [
    path('', IpListAPIView.as_view(), name="list"),
    path('external/', ExternalSourceIpOnlyListAPIView.as_view(), name="external_ip_list"),
    path('internal/', InternalSourceIpOnlyListAPIView.as_view(), name="external_ip_list"),
    path('create/', IpCreateAPIView.as_view(), name="create"),
]
