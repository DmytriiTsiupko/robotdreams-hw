from django.urls import path
from .views import UserListViews, UserDetailView, UserFormView


urlpatterns = [
    path('', UserListViews.as_view(), name='user-list'),
    path('<int:id>', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserFormView.as_view(), name='user-create')
]
