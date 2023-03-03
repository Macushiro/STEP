from django.db import models


class Course(models.Model):
    """
    Course model description
    """
    name = models.CharField(
        verbose_name="Наименование курса/Course name",
        max_length=256,
        blank=False,
        editable=True,
    )
    description = models.TextField(
        verbose_name="О курсе/Description", blank=True, null=True
    )
    is_available = models.BooleanField(
        verbose_name="Доступен/Available", blank=True, null=True
    )