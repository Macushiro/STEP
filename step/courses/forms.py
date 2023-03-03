"""
    Описание форм для вывода/получения данных.
"""

from django import forms

from employees.models import Employee
from .models import Course


class CourseModelForm(forms.ModelForm):
    """
    Custom form for Course model
    """
    name = forms.CharField(
        label="Наименование курса/Course name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        label="О курсе/Description",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    is_available = forms.BooleanField(
        label="Доступен/Available",
        initial=True,
        widget=forms.CheckboxInput(attrs={"checked": True}),
    )


    class Meta:
        """
        Meta for Course custom model form
        """
        model = Course
        fields = ("name", "description", "is_available")
