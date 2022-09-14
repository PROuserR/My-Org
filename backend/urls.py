from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
]