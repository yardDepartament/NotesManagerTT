from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NoteViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем NoteViewSet с путем 'notes/' и базовым именем 'note'
router.register(r'notes', NoteViewSet, basename='note')

# Определяем urlpatterns, включая пути созданные маршрутизатором
urlpatterns = [
    path('', include(router.urls)),  # Включаем пути из маршрутизатора
]
