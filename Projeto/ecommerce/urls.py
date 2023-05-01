
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', include('loja.urls')),
    path(r'auth/', include('djoser.urls')),
    path (r'auth/', include('djoser.urls.jwt')),
    path(r'auth/', include('djoser.urls.authtoken')), #add o endpoint que queremos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


