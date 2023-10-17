from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('tag/<str:tag>/', views.posttag, name='posttag'),
    path('create/', views.postcreate, name='postcreate'),
    path('update/<int:pk>/', views.postupdate, name='postupdate'),
    path('delete/<int:pk>/', views.postdelete, name='postdelete'),
    # path('testlogout/', views.posttest, name='posttest'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
