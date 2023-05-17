from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import UserForm

from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserListView(ListView):
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


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
