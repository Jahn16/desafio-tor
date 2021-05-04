from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import IpSerializer
from .pagination import IPPageNumberPagination
from ..models import Ip

from utils import tor_data


class IpListAPIView(ListAPIView):
    """Display all the IPs from external sources and from the internal database"""
    serializer_class = IpSerializer
    pagination_class = IPPageNumberPagination

    def get_queryset(self):
        """Gets the list with objects that will be displayed

        :return: List with IPs from external sources and from the internal database
        """
        tor_nodes = tor_data.get_tor_nodes()
        tor_hostnames = tor_data.get_tor_relays_exit_addresses()
        ips = list(Ip.objects.all())
        for tor_node in tor_nodes:
            tor_node_ip = Ip()
            tor_node_address = str(tor_node).replace('\n', '')
            tor_node_ip.ip_address = tor_node_address
            ips.append(tor_node_ip)
        for tor_hostname in tor_hostnames:
            tor_hostname_ip = Ip()
            tor_hostnames_address = tor_hostname
            tor_hostname_ip.ip_address = tor_hostnames_address
            ips.append(tor_hostname_ip)
        queryset = ips
        return queryset


class ExternalSourceIpOnlyListAPIView(IpListAPIView):
    """Display all the IPs from external sources"""
    def get_queryset(self):
        """Gets the list with objects that will be displayed

        :return: List with all IPs from external sources
        """
        queryset = super().get_queryset()
        data_base_ips = Ip.objects.all()
        queryset = queryset[len(data_base_ips):]
        return queryset


class InternalSourceIpOnlyListAPIView(IpListAPIView):
    """Display all the IPs from the internal database"""
    def get_queryset(self):
        """Gets the list with objects that will be displayed

        :return: List with all IPs from internal database
        """
        data_base_ips = Ip.objects.all()
        queryset = data_base_ips
        return queryset


class IpCreateAPIView(CreateAPIView):
    serializer_class = IpSerializer
