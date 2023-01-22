from account.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from curator.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_CURATOR_FULL_NAME,
)


class CuratorViewTest(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.curator_data = {
            "email": TEST_CURATOR_EMAIL,
            "full_name": TEST_CURATOR_FULL_NAME,
            "gender": TEST_GENDER,
            "age": TEST_AGE,
            "password": TEST_PASSWORD,
        }
        self.client.force_authenticate(self.admin)
        self.list_path = reverse("curator:list")
        self.response = self.client.post(path=self.list_path, data=self.curator_data)
        self.detail_path = reverse(
            "curator:detail", kwargs={"pk": self.response.json()["id"]}
        )

    def test_list_curators(self):
        response = self.client.get(path=self.list_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_curator(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read_curator(self):
        response = self.client.get(path=self.detail_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_CURATOR_EMAIL)
        self.assertContains(response, TEST_CURATOR_FULL_NAME)
        self.assertContains(response, TEST_GENDER)
        self.assertContains(response, TEST_AGE)

    def test_update_curator(self):
        self.curator_data["full_name"] = TEST_UPDATED_CURATOR_FULL_NAME
        response = self.client.put(
            path=self.detail_path,
            data=self.curator_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_CURATOR_FULL_NAME)

    def test_delete_curator(self):
        response = self.client.delete(
            path=self.detail_path,
            follow=True,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
