"""
    Файл тестирования моделей.
"""

from django.test import TestCase

from employees.models import Employee
from .models import Result
from courses.models import Course


# Create your tests here.
class TestEmployee(TestCase):
    """
    Test functions description for Employee model
    """

    def setUp(self) -> None:
        """
        Execute before tests starting
        :return:
        """
        print("......Created course for test......")
        self.course = Course.objects.create(name="SQL", description="SQL for dummies")

    def tearDown(self) -> None:
        """
        Execute after tests starting
        :return:
        """
        self.course.delete()
        print("....Test course has been deleted....")

    def test_str(self):
        """
        Test case for checking to_string method
        :return:
        """
        employee = Employee.objects.create(username="Frank", email="frank@sinatra.com")
        self.assertEqual(str(employee.username), "Frank")
        self.assertEqual(str(employee.email), "frank@sinatra.com")

    def test_create_with_course(self):
        """
        Test case for checking Course create functionality
        :return:
        """
        employee = Employee.objects.create(
            username="Frank", email="frank@sinatra.com", course=self.course
        )
        self.assertTrue(employee.course.name, self.course.name)
        Employee.objects.filter(pk=employee.pk).update(course="")

    def test_update(self):
        """
        Test case for checking Course updating functionality
        :return:
        """
        employee = Employee.objects.create(username="Frank", email="frank@sinatra.com")
        Employee.objects.filter(pk=employee.pk).update(course=self.course)
        employee.refresh_from_db()
        self.assertEqual(employee.course, self.course)
        Employee.objects.filter(pk=employee.pk).update(course="")


class TestCourse(TestCase):
    """
    Test functions description for Course model
    """

    def test_str_method(self):
        """
        Test case for checking to_string method
        :return:
        """
        course = Course.objects.create(name="SQL")
        self.assertEqual(str(course.name), "SQL")

    def test_update(self):
        """
        Test case for checking Course updating functionality
        :return:
        """
        course = Course.objects.create(name="SQL")
        Course.objects.filter(pk=course.pk).update(description="SQL for dummies")
        course.refresh_from_db()
        self.assertEqual(str(course.description), "SQL for dummies")

    def test_wrong(self):
        """
        Test case for checking Course incorrect creating
        :return:
        """
        course = Course.objects.create(name=00000000000, description=111111111)
        with self.assertRaises(AssertionError):
            self.assertEqual(course.name, "00000000000")
            self.assertEqual(course.description, "111111111")
            print("Get expected error")


class TestResult(TestCase):
    """
    Test functions description for Result model
    """

    def test_result_init(self):
        """
        Test case for checking Result create functionality
        :return:
        """
        course = Course.objects.create(name="SQL")
        employee = Employee.objects.create(
            username="Frank", email="frank@sinatra.com", course=course
        )
        result = Result.objects.create(
            employee=employee, course=course, percent=10.1, test_result=True
        )
        self.assertEqual(result.percent, 10.1)
        self.assertEqual(result.test_result, True)
