from django_filters import rest_framework as filters
from .models import Purchase


class PurchaseFilter(filters.FilterSet):
    book_id = filters.CharFilter(lookup_expr='icontains')
    user_id = filters.CharFilter(lookup_expr='icontains')
    order_date = filters.CharFilter(lookup_expr='icontains')
    total_price = filters.CharFilter(lookup_expr='icontains')
    quantity = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Purchase
        fields = ['book_id', 'user_id', 'order_date', 'total_price', 'quantity']


