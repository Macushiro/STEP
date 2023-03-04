"""
    Файл моделей приложения.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course


class Employee(AbstractUser):
    first_name = models.CharField(
        verbose_name="Имя/Name",
        max_length=128,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия/Last name",
        max_length=128,
        blank=True,
        null=True,
    )
    position = models.CharField(
        verbose_name="Должность/Position",
        max_length=128,
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        verbose_name="О себе/About your self",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
