
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import notice


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maintest.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('notice/', notice , name='notice'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)