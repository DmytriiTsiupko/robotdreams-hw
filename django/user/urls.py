from django.urls import path
from .views import UserListViews, UserDetailView





urlpatterns = [
    path('', UserListViews.as_view(), name='user_list'),
    path('<int:id>', UserDetailView.as_view(), name='user_detail')
]
