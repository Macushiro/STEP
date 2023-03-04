"""
    Файл тестирования контролеров (view).
"""

from django.test import TestCase
from courses.models import Course
from employees.models import Employee


class TestControllerView(TestCase):
    """
    Test views description
    """

    def test_response_status_code(self):
        """
        Test case for checking response status code
        :return:
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/course/list/")
        self.assertEqual(response.status_code, 200)

    def test_course_detail(self):
        """
        Test case for checking Course detail URL
        :return:
        """
        employee = Employee.objects.create_user(
            username="Frank", email="Frank@email.com", password="Frank1234567"
        )
        self.client.login(username="Frank", password="Frank1234567")

        response = self.client.get("/course/detail/88888888/")
        self.assertEqual(response.status_code, 404)

        course = Course.objects.create(name="SQL")
        response = self.client.get(f"/course/detail/{course.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        """
        Test case for checking response context
        :return:
        """
        course = Course.objects.create(name="SQL", is_available=True)
        response = self.client.get("/course/list/")
        self.assertEqual(response.context["courses"].first().name, "SQL")

    def test_response_content(self):
        """
        Test case for checking response content
        :return:
        """
        response = self.client.get("/course/list/")
        button = '<a class="btn btn-outline-primary my-3"\n       href="/"\n    >Back to main page</a>'
        self.assertIn(button, response.content.decode(encoding="utf-8"))

    def test_permissions(self):
        """
        Test case for checking site functionality accessing
        :return:
        """
        # For unauthorized employee
        response = self.client.get("/employee/list/")
        self.assertEqual(response.status_code, 302)

        # For authorized employee
        employee = Employee.objects.create_user(
            username="Frank", email="Frank@email.com", password="Frank1234567"
        )
        self.client.login(username="Frank", password="Frank1234567")
        self.assertEqual(response.status_code, 302)

        response = self.client.get("/employee/info/")
        self.assertEqual(response.status_code, 200)

        # For just logout employee
        self.client.logout()
        response = self.client.get("/employee/info/")
        self.assertEqual(response.status_code, 302)

        # Check superuser permissions
        response = self.client.get("/employee/list/")
        self.assertEqual(response.status_code, 302)
        employee = Employee.objects.create_superuser(
            username="test_admin",
            email="test_admin@email.com",
            password="test_admin1234567",
        )
        self.client.login(username="test_admin", password="test_admin1234567")
        response = self.client.get("/employee/list/")
        self.assertEqual(response.status_code, 200)
