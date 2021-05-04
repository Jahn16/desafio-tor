"""
Module containing functions that retrieve Tor related data from external sources
"""
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString


def get_tor_nodes():
    """Returns a list of Tor Nodes obtained from a website

    :return: list of NavigableStrings containing a Tor Node
    """
    def filter_tor_node_html(tor_node):
        """Filter non NavigableString or empty elements

        :param tor_node: tor_node to be filtered

        :return: True if its a valid Tor Node
        """
        return isinstance(tor_node, NavigableString) and not isinstance(tor_node, Comment) and tor_node != "\n"

    url = 'https://www.dan.me.uk/tornodes'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    tor_node_list_begin = soup.find(string=lambda text: isinstance(text, Comment)
                                    and (str(text) == " __BEGIN_TOR_NODE_LIST__ //"))
    tor_nodes = list(filter(filter_tor_node_html, tor_node_list_begin.next_siblings))
    return tor_nodes


def get_tor_relays_exit_addresses():
    """Returns a list of Tor Nodes obtained from a website

    :return: List of Strings containing an exit address
    """
    url = 'https://onionoo.torproject.org/summary?limit=5000'
    request = requests.get(url)
    relays = request.json()['relays']
    exit_addresses = []
    for relay in relays:
        relay_exit_addresses = relay['a']
        exit_addresses += relay_exit_addresses
    return exit_addresses
