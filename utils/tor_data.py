import requests
from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString

def get_tor_nodes():
    def filter_tor_node_html(tor_node):
        return isinstance(tor_node, NavigableString) and not isinstance(tor_node, Comment) and tor_node != "\n"

    external_source = 'https://www.dan.me.uk/tornodes'
    request = requests.get(external_source)
    soup = BeautifulSoup(request.text, 'html.parser')
    tor_node_list_begin = soup.find(string=lambda text: isinstance(text, Comment)
                                    and (str(text) == " __BEGIN_TOR_NODE_LIST__ //"))
    tor_nodes = list(filter(filter_tor_node_html, tor_node_list_begin.next_siblings))
    return tor_nodes


def get_tor_relays_exit_addresses():
    external_source = 'https://onionoo.torproject.org/summary?limit=5000'
    request = requests.get(external_source)
    relays = request.json()['relays']
    exit_addresses = []
    for relay in relays:
        relay_exit_addresses = relay['a']
        exit_addresses += relay_exit_addresses
    return exit_addresses



