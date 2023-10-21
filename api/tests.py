from django.test import TestCase
from .models import Note
from .serializers import NoteSerializer
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class NoteModelTest(TestCase):
    """
    Класс для тестирования модели Note.

    Methods:
    ````setUpTestData(cls): Создает тестовую заметку.
    ````test_title_max_length(self): Проверяет максимальную длину заголовка.
    ````test_content(self): Проверяет содержимое заметки.
    ````test_created_at_auto_now_add(self): Проверяет автоматическое добавление времени создания.
    ````test_empty_title_not_allowed(self): Проверяет, что пустой заголовок не допускается.

    """
    @classmethod
    def setUpTestData(cls):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_title_max_length(self):
        """
        Проверка максимальной длины заголовка.
        """
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_content(self):
        """
        Проверка содержимого заметки.
        """
        note = Note.objects.get(id=1)
        content = note.content
        self.assertEqual(content, 'This is a test note.')

    def test_created_at_auto_now_add(self):
        """
        Проверка автоматического добавления времени создания.
        """
        note = Note.objects.get(id=1)
        created_at = note.created_at
        self.assertIsNotNone(created_at)

    def test_empty_title_not_allowed(self):
        """
        Проверка, что пустой заголовок не допускается.
        """
        note = Note(content='This is a test note.')
        with self.assertRaises(Exception):
            note.full_clean()


class NoteSerializerTests(TestCase):
    """
    Класс для тестирования сериализатора Note.

    Methods:
    ````test_serializer_data(self): Проверяет данные сериализатора.

    """

    def test_serializer_data(self):
        """
        Проверка данных сериализатора.
        """
        note_data = {'title': 'Test Note', 'content': 'This is a test note.'}
        serializer = NoteSerializer(data=note_data)
        self.assertTrue(serializer.is_valid())


class NoteViewSetTests(TestCase):
    """
    Класс для тестирования ViewSet Note.

    Methods:
    ````setUp(self): Инициализация клиента и данных для тестирования.
    ````test_create_note(self): Проверка создания заметки.
    ````test_view_note_list(self): Проверка просмотра списка заметок.
    ````test_view_note_detail(self): Проверка просмотра деталей заметки.
    ````test_update_note(self): Проверка обновления заметки.
    ````test_delete_note(self): Проверка удаления заметки.

    """

    def setUp(self):
        self.client = APIClient()
        self.note_data = {'title': 'Test Note',
                          'content': 'This is a test note.'}

    def test_create_note(self):
        """
        Проверка создания заметки.
        """
        response = self.client.post(
            reverse('note-list'), self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_view_note_list(self):
        """
        Проверка просмотра списка заметок.
        """
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_note_detail(self):
        """
        Проверка просмотра деталей заметки.
        """
        note = Note.objects.create(
            title="Test Note", content="This is a test note.")
        response = self.client.get(
            reverse('note-detail', kwargs={'pk': note.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        """
        Проверка обновления заметки.
        """
        note = Note.objects.create(
            title="Test Note", content="This is a test note.")
        updated_data = {'title': 'Updated Test Note',
                        'content': 'Updated content'}
        response = self.client.put(
            reverse('note-detail', kwargs={'pk': note.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Test Note')

    def test_delete_note(self):
        """
        Проверка удаления заметки.
        """
        note = Note.objects.create(
            title="Test Note", content="This is a test note.")
        response = self.client.delete(
            reverse('note-detail', kwargs={'pk': note.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
