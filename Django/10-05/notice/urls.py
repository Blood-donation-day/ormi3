from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice, name = 'notice'),
    path('free/', views.free, name = '자유게시판 목록'),
    path('free/<int:aa>', views.frees, name = '자유게시판 상세 게시물'),
    path('oneone/', views.oneone, name = '1 대 1 상담 안내'),
    path('oneone/<int:ones>', views.oneones, name = '1 대 1 상담 상세 게시물'),
]