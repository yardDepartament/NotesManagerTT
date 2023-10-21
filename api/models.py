from django.db import models


class Note(models.Model):
    """
    Модель для заметок.

    Атрибуты:
        title (str): Заголовок заметки.
        content (str): Содержимое заметки.
        created_at (datetime): Дата время создания, создаётся автоматически при добавлении объекта.

    Methods:
        __str__: возвращает заголовок заметки.
        update_content: Обновляет содержимое заметки.
        delete_note: Удаляет заметку.

    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает заголовок заметки.

        Returns:
            str: Заголовок заметки.

        """
        return self.title

    def update_content(self, new_content):
        """
        Обновляет содержимое заметки.

        Args:
            new_content (str): Новое содержимое заметки.

        Returns:
            None

        """
        self.content = new_content
        self.save()

    def delete_note(self):
        """
        Удаляет заметку.

        Returns:
            None

        """
        self.delete()
