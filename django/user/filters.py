import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age']
