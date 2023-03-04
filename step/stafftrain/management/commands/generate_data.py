"""
    Файл наполнения БД.
"""

import os
import random

import requests
from django.core.exceptions import BadRequest
from django.core.management.base import BaseCommand
from django.db import IntegrityError

import env
from courses.models import Course
from employees.models import Employee
from stafftrain.models import Result

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
course_list = [
    "SQL",
    "Python",
    "Java",
    "Kotlin",
    "JS",
    "HTML/CSS",
    "JQuery",
    "C++",
    "Scala",
]
course_level = [
    "starter",
    "base",
    "advanced",
    "professional",
    "for architects",
    "for experts",
    "optimization",
]


class Command(BaseCommand):
    """
    Custom command for data generation
    """
    help = "Generate data"

    def handle(self, *args, **options):
        """
        command function
        :param args: 
        :param options: 
        :return: 
        """
        print("DB populating has started")

        # 1. Clearing
        print("Erasing previous data")
        Result.objects.all().delete()
        Course.objects.all().delete()
        Employee.objects.all().delete()

        # 2. Generate base data
        print("Generating examples data")
        # 2.0 Create superuser
        super_user = Employee.objects.create_superuser(
            username="macushiro",
            email="macushiro@newbie.com",
            password=env.super_user,
        )
        # 2.1 Generate courses data
        rand = random
        for course in course_list:
            try:
                course_name = rand.choice(course_list)
                course = Course.objects.create(
                    name=course_name,
                    description=f"{course_name} {rand.choice(course_level)} course",
                    is_available=True,
                )
                print(course.name, course.description)
            except IntegrityError:
                raise BadRequest(f"Couldn't write data into Database.")
        courses = Course.objects.all()

        # 2.2 Getting data from external service
        with requests.session() as session:
            response = session.get(USERS_DATA_URL)
            data = response.json()
            # 2.3 Generate employees data
            for elem in data:
                try:
                    employee = Employee.objects.create(
                        username=elem["username"],
                        first_name=elem["name"],
                        email=elem["email"],
                        course=rand.choice(courses)
                    )
                    print(employee.id, employee.username, employee.first_name)
                except IntegrityError:
                    raise BadRequest(f"Couldn't write data into Database.")

        # 3. Generate results data  -  for feature working
        # min_employee_id = Employee.objects.order_by('id').first()
        # max_employee_id = Employee.objects.order_by('id').last()
        # employee_list = range(min_employee_id, max_employee_id + 1)
        # left_bord = 1
        # for elem in employee_list:
        #     right_bord = left_bord + rand.randrange(1, 10)
        #     while left_bord < right_bord:
        #         result = Result.objects.create(
        #             employee=elem,
        #             course=f"Result #{left_bord} for {rand.choice(['normal', 'good', 'great'])}",
        #             percent=rand.uniform(1.0, 100.0),
        #             test_result=left_bord,
        #         )
        #         left_bord += 1
        #     left_bord = right_bord
