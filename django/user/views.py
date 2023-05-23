from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework import filters

from .models import User
from .forms import UserForm
from .serializers import UserSerializer
from .pagination import UserResultsSetPagination
from .filters import UserFilter


# ==== VIEWS ====

class UserListView(ListAPIView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user-list'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user-detail'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user-list')


# ==== VIEW SETS ====

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserResultsSetPagination
    filterset_class = UserFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['age', 'id']
    search_fields = ['first_name', 'last_name', 'age']
