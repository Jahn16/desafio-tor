from rest_framework.pagination import PageNumberPagination


class IPPageNumberPagination(PageNumberPagination):
    page_size = 10
