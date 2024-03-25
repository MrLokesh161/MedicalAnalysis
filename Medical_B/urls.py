from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from api.views import CustomAuthToken




urlpatterns = [
    path('admin/', admin.site.urls),
    path('obtainAuthToken/',CustomAuthToken.as_view()),
    path('', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)