from account.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from curator.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_UPDATED_CURATOR_FULL_NAME,
    TEST_AGE,
    TEST_GENDER,
    TEST_PASSWORD,
)

from curator.models import Curator


class CuratorAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.client.force_authenticate(self.admin_user)
        self.curator_data = {
            "email": TEST_CURATOR_EMAIL,
            "full_name": TEST_CURATOR_FULL_NAME,
            "gender": TEST_GENDER,
            "age": TEST_AGE,
            "password": TEST_PASSWORD,
        }
        self.response = self.client.post(
            reverse("curator:list"), self.curator_data, format="json"
        )

    def test_create_curator(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read_curator(self):
        curator = Curator.objects.get(email=TEST_CURATOR_EMAIL)
        response = self.client.get(
            reverse("curator:detail", kwargs={"pk": curator.pk}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, TEST_CURATOR_EMAIL)
        self.assertContains(response, TEST_CURATOR_FULL_NAME)
        self.assertContains(response, TEST_GENDER)
        self.assertContains(response, TEST_AGE)

    def test_update_curator(self):
        curator = Curator.objects.get(email=TEST_CURATOR_EMAIL)
        self.curator_data["full_name"] = TEST_UPDATED_CURATOR_FULL_NAME
        response = self.client.put(
            reverse("curator:detail", kwargs={"pk": curator.pk}),
            self.curator_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_CURATOR_FULL_NAME)

    def test_delete_curator(self):
        curator = Curator.objects.get(email=TEST_CURATOR_EMAIL)
        response = self.client.delete(
            reverse("curator:detail", kwargs={"pk": curator.pk}),
            format="json",
            follow=True,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
