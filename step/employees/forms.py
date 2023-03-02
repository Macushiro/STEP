"""
    Описание форм для вывода/получения данных.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from employees.models import Employee


class RegistrationForm(UserCreationForm):
    """
    Custom form for Employee model object registration
    """
    username = forms.CharField(help_text="Введите логин", label="Логин/Login:")
    email = forms.CharField(help_text="Введите Вашу почту", label="Почта/Email:")
    first_name = forms.CharField(help_text="Введите Ваше имя", label="Имя/Name:")
    last_name = forms.CharField(
        help_text="Введите Вашу фамилию", label="Фамилия/Last Name:"
    )
    position = forms.CharField(help_text="Должность/Position", label="Должность/Position:")
    about_me = forms.CharField(help_text="Напишите немного о себе", label="О себе/About me:")
    password1 = forms.CharField(
        help_text="Введите пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        help_text="Введите повторно пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )

    class Meta:
        """
        Meta for Employee custom model form
        """
        model = Employee
        # model = Student   - for future functional extending
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "position",
            "about_me",
            "password1",
            "password2",
        )


class EmployeeUpdateForm(UserChangeForm):
    """
    Custom form for Employee model object updating
    """
    username = forms.CharField(help_text="Введите логин", label="Логин/Login:")
    email = forms.CharField(help_text="Введите Вашу почту", label="Почта/Email:")
    first_name = forms.CharField(help_text="Введите Ваше имя", label="Имя/Name:")
    last_name = forms.CharField(
        help_text="Введите Вашу фамилию", label="Фамилия/Last Name:"
    )
    position = forms.CharField(help_text="Должность/Position", label="Должность/Position:")
    about_me = forms.CharField(help_text="Напишите немного о себе", label="О себе/About me:")
    password1 = forms.CharField(
        help_text="Введите пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        help_text="Введите повторно пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )

    class Meta:
        """
        Meta for Employee custom model form
        """
        model = Employee
        # model = Student   - for future functional extending
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "position",
            "about_me",
            "password1",
            "password2",
        )
