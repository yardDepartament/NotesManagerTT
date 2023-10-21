from rest_framework import viewsets
from rest_framework import filters
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обеспечения всех CRUD операция c объектом.



    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
