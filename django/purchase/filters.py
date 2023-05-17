import django_filters
from .models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    book_id = django_filters.CharFilter(lookup_expr='icontains')
    user_id = django_filters.CharFilter(lookup_expr='icontains')
    order_date = django_filters.CharFilter(lookup_expr='icontains')
    total_price = django_filters.NumberFilter(lookup_expr='icontains')
    quantity = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = Purchase
        fields = ['book_id', 'user_id', 'order_date', 'total_price', 'quantity']


