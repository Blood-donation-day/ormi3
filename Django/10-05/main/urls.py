from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name= 'home'),
    
    path('about/', views.about, name= 'about'),
    
    path('product/', views.product, name= 'product-page'),
    path('product/<int:pk>', views.products, name= 'product-pages'),
    
    path('contact/', views.contact, name= 'contact'),
    
    path('qna/', views.qna, name= 'qna'),
    path('qna/<int:qnas>', views.qnas, name= 'qna-pages'),
]