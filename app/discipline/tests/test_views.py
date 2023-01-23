from account.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from discipline.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_AGE,
    TEST_DISCIPLINE_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_DISCIPLINE_NAME,
)


class DisciplineViewTest(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.discipline_data = {"name": TEST_DISCIPLINE_NAME}
        self.client.force_authenticate(self.admin)
        self.list_path = reverse("discipline:list")
        self.response = self.client.post(path=self.list_path, data=self.discipline_data)
        self.detail_path = reverse("discipline:detail", kwargs={"pk": self.response.json()["id"]})

    def test_list_disciplines(self):
        response = self.client.get(path=self.list_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_discipline(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read_discipline(self):
        response = self.client.get(path=self.detail_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], TEST_DISCIPLINE_NAME)

    def test_update_discipline(self):
        self.discipline_data["name"] = TEST_UPDATED_DISCIPLINE_NAME
        response = self.client.put(path=self.detail_path, data=self.discipline_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_DISCIPLINE_NAME)

    def test_delete_discipline(self):
        response = self.client.delete(path=self.detail_path, follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
