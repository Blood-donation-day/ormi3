from django.urls import path, include
from .views import (
    UserCreateView,
    UserDetailView,
)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]