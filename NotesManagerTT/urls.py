from django.contrib import admin
from django.urls import path, include
import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
