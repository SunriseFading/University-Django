from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from account.models import CustomUser
from account.tests.settings import (
    TEST_EMAIL,
    TEST_FULL_NAME,
    TEST_WRONG_PASSWORD,
    TEST_PASSWORD,
    TEST_AGE,
    TEST_GENDER,
)

class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email=TEST_EMAIL,
            password=TEST_PASSWORD,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE
        )
        self.client = APIClient()

    def test_login_success(self):
        response = self.client.post(reverse('account:login'), {'email': TEST_EMAIL, "password": TEST_PASSWORD})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_login_failure(self):
        response = self.client.post(reverse('account:login'), {'email': TEST_EMAIL, "password": TEST_WRONG_PASSWORD})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('error' in response.data)

class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email=TEST_EMAIL,
            password=TEST_PASSWORD,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_logout_success(self):
        response = self.client.get(reverse('account:logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
