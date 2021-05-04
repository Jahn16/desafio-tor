from django.views.generic import ListView, CreateView

from .models import Ip

from utils import tor_data

app_name = 'ips'

class IpListView(ListView):
    model = Ip
    template_name = 'ips/list.html'
    context_object_name = 'ips'
    paginate_by = 10
    def get_queryset(self):
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


class ExternalSourceIpOnlyListView(IpListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        data_base_ips = Ip.objects.all()
        queryset = queryset[len(data_base_ips):]
        return queryset


class InternalSourceIpOnlyListView(IpListView):
    def get_queryset(self):
        data_base_ips = Ip.objects.all()
        queryset = data_base_ips
        return queryset



