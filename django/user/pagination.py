from rest_framework.pagination import PageNumberPagination


class UserResultsSetPagination(PageNumberPagination):
    page_size = 10
