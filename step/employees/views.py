"""
    Файл классов-обработчиков запросов к приложению.
"""

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
)

from stafftrain.models import Course
from employees.forms import RegistrationForm, EmployeeUpdateForm, EmployeeCourseJoinForm
from employees.models import Employee


class EmployeeRegistrationView(CreateView):
    """
    Employee registration controller
    """

    model = Employee
    form_class = RegistrationForm
    success_url = "/"
    template_name = "employee_form.html"


class EmployeeLoginView(LoginView):
    """
    Employee login controller
    """

    template_name = "login_form.html"


class EmployeeLogoutView(LoginRequiredMixin, LogoutView):
    """
    Employee logout controller
    """

    pass


class EmployeeListView(UserPassesTestMixin, ListView):
    """
    Students list controller
    """

    model = Employee
    context_object_name = "employees"
    template_name = "employees_list.html"

    def test_func(self):
        """
        Function for employees privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        """
        The function of obtaining objects of the Employee model
        :return:
        """
        return Employee.objects.filter(is_staff=False)

    def get_context_data(self, **kwargs):
        """
        Function for context extension
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        print(context["courses"])
        return context


class EmployeeDetailView(LoginRequiredMixin, TemplateView):
    """
    Employee detail info controller
    """

    template_name = "employee_detail.html"


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """
    Employee info updating controller
    """

    model = Employee
    template_name = "employee_update_form.html"
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy("employee_info")


class EmployeeJoinCourseView(LoginRequiredMixin, UpdateView):
    """
    Employee info updating controller
    """

    model = Employee
    template_name = "employee_join_course_form.html"
    form_class = EmployeeCourseJoinForm
    success_url = reverse_lazy("courses_list")


class EmployeeDeleteView(UserPassesTestMixin, DeleteView):
    """
    Employee deleting controller
    """

    model = Employee
    template_name = "employee_confirm_delete.html"
    success_url = reverse_lazy("employees_list")

    def test_func(self):
        """
        Function for employees privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser
