from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:id>', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create')
]
