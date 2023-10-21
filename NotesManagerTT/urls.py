from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Путь к админ-панели Django
    path('admin/', admin.site.urls),
    
    # Путь к API версии 1
    path('api/v1/', include('api.urls')),
]
