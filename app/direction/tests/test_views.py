from account.models import CustomUser
from curator.models import Curator
from discipline.models import Discipline
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from direction.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_DIRECTION_NAME,
    TEST_DISCIPLINE_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_DIRECTION_NAME,
)


class DirectionViewTest(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.discipline = Discipline.objects.create(name=TEST_DISCIPLINE_NAME)
        self.direction_data = {
            "name": TEST_DIRECTION_NAME,
            "curator": self.curator.id,
            "disciplines": [self.discipline.id],
        }
        self.client.force_authenticate(self.admin)
        self.list_path = reverse("direction:list")
        self.response = self.client.post(path=self.list_path, data=self.direction_data)
        self.detail_path = reverse("direction:detail", kwargs={"pk": self.response.json()["id"]})

    def _direction(self):
        response = self.client.get(path=self.list_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_direction(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read_direction(self):
        response = self.client.get(path=self.detail_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], TEST_DIRECTION_NAME)
        self.assertEqual(response.data["curator"], self.curator.id)
        self.assertEqual(response.data["disciplines"], [self.discipline.id])

    def test_update_direction(self):
        self.direction_data["name"] = TEST_UPDATED_DIRECTION_NAME
        response = self.client.put(path=self.detail_path, data=self.direction_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_DIRECTION_NAME)

    def test_delete_direction(self):
        response = self.client.delete(path=self.detail_path, follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
