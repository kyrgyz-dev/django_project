from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Биография"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
        verbose_name="Аватар"
    )

    def __str__(self):
        return f'Профиль {self.user.username}'

