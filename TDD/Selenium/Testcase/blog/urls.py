from django.urls import path
from . import views
urlpatterns =[
    path('about/', views.PostList.as_view(), name='about'),
    path('contact/', views.PostList.as_view(), name='contact'),
    path('blog/', views.PostList.as_view(), name='postlist'),
    path('blog/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
]