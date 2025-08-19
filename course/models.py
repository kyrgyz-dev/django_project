from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name="Описание")

    students = models.ManyToManyField(
        to=User,
        related_name='courses',
    )
