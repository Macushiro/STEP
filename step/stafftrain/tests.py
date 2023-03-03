"""
    Файл тестирования моделей.
"""

from django.test import TestCase

from employees.models import Employee
from .models import Result
from courses.models import Course

#
# # Create your tests here.
# class TestEmployee(TestCase):
#     """
#     Test functions description for Employee model
#     """
#     def test_str(self):
#         """
#         Test case for checking to_string method
#         :return:
#         """
#         user = Employee.objects.create(username="Frank", email="frank@sinatra.com")
#         self.assertEqual(str(user.username), "Frank")
#         self.assertEqual(str(user.email), "frank@sinatra.com")
#
#
# class TestCourse(TestCase):
#     """
#     Test functions description for Course model
#     """
#     def setUp(self) -> None:
#         """
#         Execute before tests starting
#         :return:
#         """
#         print("......Created user for test......")
#         self.user = Employee.objects.create(username="Frank", email="frank@sinatra.com")
#
#     def tearDown(self) -> None:
#         """
#         Execute after tests starting
#         :return:
#         """
#         self.user.delete()
#         print("....Test user has been deleted....")
#
#     def test_str_method(self):
#         """
#         Test case for checking to_string method
#         :return:
#         """
#         course = Course.objects.create(name="SQL")
#         self.assertEqual(str(course.name), "SQL")
#
#     def test_create_with_employee(self):
#         """
#         Test case for checking Course create functionality
#         :return:
#         """
#         course = Course.objects.create(name="SQL", employee=self.user)
#         self.assertTrue(course.employee, self.user)
#         Course.objects.filter(pk=course.pk).update(employee="")
#
#     def test_update(self):
#         """
#         Test case for checking Course updating functionality
#         :return:
#         """
#         course = Course.objects.create(name="SQL", employee=self.user)
#         Course.objects.filter(pk=course.pk).update(name="Python")
#         course.refresh_from_db()
#         self.assertEqual(str(course.name), "Python")
#         Course.objects.filter(pk=course.pk).update(employee="")
#
#     def test_wrong(self):
#         """
#         Test case for checking Course incorrect creating
#         :return:
#         """
#         course = Course.objects.create(name=00000000000, description=111111111)
#         with self.assertRaises(AssertionError):
#             self.assertEqual(course.name, "00000000000")
#             self.assertEqual(course.description, "111111111")
#             print("Get expected error")
#
#
# class TestResult(TestCase):
#     """
#     Test functions description for Result model
#     """
#     def test_result_init(self):
#         """
#         Test case for checking Result create functionality
#         :return:
#         """
#         user = Employee.objects.create(username="Frank", email="frank@sinatra.com")
#         course = Course.objects.create(name="SQL", employee=user)
#         result = Result.objects.create(
#             employee=user, course=course, percent=10.1, test_result=True
#         )
#         self.assertEqual(result.percent, 10.1)
#         self.assertEqual(result.test_result, True)
