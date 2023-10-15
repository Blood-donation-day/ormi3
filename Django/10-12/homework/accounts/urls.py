from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    
    # 로그인한 사용자만 볼 수 있게 해야해.
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
]