from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    age = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name', 'age', 'last_name']
