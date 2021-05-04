from rest_framework.pagination import PageNumberPagination


class IPPageNumberPagination(PageNumberPagination):
    """Paginates the IPs by 10
    """
    page_size = 10
