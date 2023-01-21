from curator.models import Curator
from direction.models import Direction
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from group.models import Group
from group.tests.settings import (
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_DIRECTION_NAME,
    TEST_GENDER,
    TEST_GROUP_NAME,
    TEST_PASSWORD,
    TEST_UPDATED_GROUP_NAME,
)


class GroupViewTest(APITestCase):
    def setUp(self):
        self.curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.direction = Direction.objects.create(
            name=TEST_DIRECTION_NAME, curator=self.curator
        )
        self.group_data = {
            "name": TEST_GROUP_NAME,
            "direction": self.direction.id,
        }
        self.client.force_authenticate(user=self.curator)
        self.list_path = reverse("group:list")
        self.response = self.client.post(path=self.list_path, data=self.group_data)
        self.detail_path = reverse(
            "group:detail", kwargs={"pk": self.response.json()["id"]}
        )

    def test_list_group(self):
        response = self.client.get(path=self.list_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_group(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read_group(self):
        response = self.client.get(path=self.detail_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], TEST_GROUP_NAME)
        self.assertEqual(response.data["direction"], self.direction.id)
        self.assertEqual(response.data["number_students"], 0)

    def test_update_group(self):
        self.group_data["name"] = TEST_UPDATED_GROUP_NAME
        response = self.client.put(path=self.detail_path, data=self.group_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_GROUP_NAME)

    def test_delete_group(self):
        response = self.client.delete(
            path=self.detail_path,
            follow=True,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
