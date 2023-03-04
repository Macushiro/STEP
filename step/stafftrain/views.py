"""
    Файл классов-обработчиков запросов к приложению.
"""

from django.contrib.auth.decorators import login_required
from django.core import management
from django.shortcuts import render
from django.views.generic import (
    ListView,
)

from courses.models import Course


class MainPageView(ListView):
    """
    Main page controller
    """
    model = Course
    context_object_name = "courses"
    template_name = "index.html"

    def get_queryset(self):
        """
        The function of obtaining objects of the Course model
        :return:
        """
        return Course.objects.all()


@login_required()
def generate_data(request):
    """
    The function for test data generation
    :param request:
    :return:
    """
    management.call_command("generate_data")
    return render(request, "index.html")
