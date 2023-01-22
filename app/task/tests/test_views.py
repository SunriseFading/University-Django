import os

from account.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from task.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_AGE,
    TEST_GENDER,
    TEST_PASSWORD,
)


class TaskViewTest(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.client.force_authenticate(self.admin)
        self.create_report_path = reverse("task:create_report")
        self.response = self.client.post(path=self.create_report_path)
        self.retrive_report_path = reverse(
            "task:retrive_report", kwargs={"task_id": self.response.json()["task_id"]}
        )

    def test_create_report(self):
        self.assertEqual(self.response.status_code, status.HTTP_202_ACCEPTED)

    def test_retrive_report(self):
        response = self.client.get(path=self.retrive_report_path)
        while (
            response["Content-Type"]
            != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            response = self.client.get(path=self.retrive_report_path)
        self.assertTrue(os.path.exists("media/report.xlsx"))
