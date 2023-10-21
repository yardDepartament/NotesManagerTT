from rest_framework import viewsets
from rest_framework import filters
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обеспечения всех CRUD операций с объектом 'Note'.

    Позволяет создавать, просматривать, обновлять и удалять заметки.

    Attributes:
    ````queryset (QuerySet): Запрос для получения всех объектов Note.
    ````serializer_class (Serializer): Сериализатор для объектов Note.
    ````filter_backends (list): Список фильтров для поиска заметок.
    ````search_fields (list): Список полей, по которым производится поиск.

    Methods:
    ````create(request): Создает новую заметку.
    ````list(request): Возвращает список всех заметок.
    ````retrieve(request, pk): Возвращает детали конкретной заметки.
    ````update(request, pk): Обновляет детали заметки.
    ````destroy(request, pk): Удаляет заметку.
        
    Применение:
    ````Поиск: нажмите на кнопку Filters и осуществите поиск (чувствителен к регистру)
    ````Просмотр, Обновление, Удаление конкретного объекта: перейдите по url /notes/{id} где id - идентефикатор заметки


    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
