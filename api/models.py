from django.db import models


from django.db import models

class Note(models.Model):
    """
    Модель для заметок.

    Атрибуты:
        title (str): Заголовок заметки.
        content (str): Содержимое заметки.
        created_at (datetime): Дата время создания, создаётся автоматически при добавлении обьекта.

    Methods:
        __str__: возвращает заголовок заметки.
        update_content: Обновляет содежримое заметки.
        delete_note: Удаляет заметку.


    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def update_content(self, new_content):
        self.content = new_content
        self.save()
        
    def delete_note(self):
        self.delete()
