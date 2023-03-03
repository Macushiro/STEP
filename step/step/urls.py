"""step URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from stafftrain.views import MainPageView, generate_data
from courses.views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)
from employees.views import (
    EmployeeRegistrationView,
    EmployeeLoginView,
    EmployeeLogoutView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeListView,
)

urlpatterns = [
    # base URLs
    path("", MainPageView.as_view(), name="main_page"),
    path("admin/", admin.site.urls),
    path("generate_data/", generate_data, name="generate"),
    # employees
    path("employees/list/", EmployeeListView.as_view(), name="employees_list"),
    path("employees/info/", EmployeeDetailView.as_view(), name="employee_info"),
    path("employees/create/", EmployeeRegistrationView.as_view(), name="registration"),
    path("employees/login/", EmployeeLoginView.as_view(), name="login"),
    path("employees/logout/", EmployeeLogoutView.as_view(), name="logout"),
    path("employees/update/<int:pk>/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("employees/delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee_delete"),
    # courses
    path("course/list/", CourseListView.as_view(), name="courses_list"),
    path("course/detail/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("course/create/", CourseCreateView.as_view(), name="course_create"),
    path("course/update/<int:pk>/", CourseUpdateView.as_view(), name="course_update"),
    path("course/delete/<int:pk>/", CourseDeleteView.as_view(), name="course_delete"),
    # results
    # path('results/list/', ResultListView.as_view(), name='results'),
]
