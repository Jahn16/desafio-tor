from django.urls import path

from .views import IpListView, InternalSourceIpOnlyListView, ExternalSourceIpOnlyListView


app_name = 'ips'

urlpatterns = [
    path('', IpListView.as_view(), name='list'),
    path('internal/', InternalSourceIpOnlyListView.as_view(), name='internal-list'),
    path('external/', ExternalSourceIpOnlyListView.as_view(), name='external-list'),
]
