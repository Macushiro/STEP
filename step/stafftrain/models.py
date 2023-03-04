"""
    Файл моделей приложения.
"""

from django.db import models

from courses.models import Course
from employees.models import Employee


class Result(models.Model):
    """
    Result model description
    """

    percent = models.DecimalField(
        verbose_name="Процент прохождения/Completion percent",
        decimal_places=1,
        max_digits=100,
        editable=True,
    )
    test_result = models.BooleanField(
        verbose_name="Статус теста/Test status", editable=True, default=False
    )
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)
    course = models.OneToOneField(Course, on_delete=models.PROTECT)
