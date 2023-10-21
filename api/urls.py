from django.urls import path
from .views import NoteListCreateView, NoteDetailView, NoteEditView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/<int:pk>/edit/', NoteEditView.as_view(), name='note-edit'),
]
