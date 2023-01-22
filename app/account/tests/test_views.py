from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from account.models import CustomUser
from account.tests.settings import (
    TEST_AGE,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_USER_EMAIL,
    TEST_USER_FULL_NAME,
    TEST_WRONG_PASSWORD,
)


class UserViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email=TEST_USER_EMAIL,
            password=TEST_PASSWORD,
            full_name=TEST_USER_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
        )
        self.login_path = reverse("account:login")
        self.login_data = {"email": TEST_USER_EMAIL, "password": TEST_PASSWORD}
        self.logout_path = reverse("account:logout")

    def test_login_success(self):
        response = self.client.post(
            path=self.login_path,
            data=self.login_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)

    def test_login_failure(self):
        self.login_data["password"] = TEST_WRONG_PASSWORD
        response = self.client.post(
            path=self.login_path,
            data=self.login_data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in response.data)

    def test_logout_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.logout_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
