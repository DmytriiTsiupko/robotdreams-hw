from django.views.generic import DetailView, ListView
from django.http import HttpResponse, JsonResponse
from .models import User


class UserListViews(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'
