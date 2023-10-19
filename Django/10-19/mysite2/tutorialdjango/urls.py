
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tube/', include('tube.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(pattern_name='tube:post_list')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)