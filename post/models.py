from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name='posts',
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f'{self.title}'


