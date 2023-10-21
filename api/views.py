from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating notes.

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteEditView(generics.UpdateAPIView):
    """
    View for editing an existing note.

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a note.

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
