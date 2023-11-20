
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # 테스트 로그인
    path('api-auth/', include('rest_framework.urls')),
]
