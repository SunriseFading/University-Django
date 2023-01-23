from curator.models import Curator
from direction.models import Direction
from django.urls import reverse
from group.models import Group
from rest_framework import status
from rest_framework.test import APITestCase

from student.tests.settings import (
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_DIRECTION_NAME,
    TEST_GENDER,
    TEST_GROUP_NAME,
    TEST_PASSWORD,
    TEST_STUDENT_EMAIL,
    TEST_STUDENT_FULL_NAME,
    TEST_UPDATED_STUDENT_FULL_NAME,
)


class StudentViewTest(APITestCase):
    def setUp(self):
        self.curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.direction = Direction.objects.create(name=TEST_DIRECTION_NAME, curator=self.curator)
        self.group = Group.objects.create(name=TEST_GROUP_NAME, direction=self.direction)
        self.student_data = {
            "email": TEST_STUDENT_EMAIL,
            "full_name": TEST_STUDENT_FULL_NAME,
            "group": self.group.id,
            "gender": TEST_GENDER,
            "age": TEST_AGE,
            "password": TEST_PASSWORD,
        }
        self.client.force_authenticate(user=self.curator)
        self.list_path = reverse("student:list")
        self.response = self.client.post(path=self.list_path, data=self.student_data)
        self.detail_path = reverse("student:detail", kwargs={"pk": self.response.json()["id"]})

    def test_list_students(self):
        response = self.client.get(path=self.list_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_student(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.group.students.count(), 1)

    def test_limit_students(self):
        for i in range(20):
            self.student_data["email"] = f"test{i}@test.com"
            response = self.client.post(path=self.list_path, data=self.student_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        curator = Curator.objects.create(
            email="curator1@test.com",
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        direction = Direction.objects.create(name=TEST_DIRECTION_NAME, curator=curator)
        group = Group.objects.create(name=TEST_GROUP_NAME, direction=direction)

        self.student_data["email"] = "test20@test.com"
        self.student_data["group"] = group.id
        response = self.client.post(path=self.list_path, data=self.student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.student_data["group"] = self.group.id
        response = self.client.put(path=self.detail_path, data=self.student_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.patch(path=self.detail_path, data=self.student_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_student(self):
        response = self.client.get(path=self.detail_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], TEST_STUDENT_EMAIL)
        self.assertEqual(response.data["full_name"], TEST_STUDENT_FULL_NAME)
        self.assertEqual(response.data["group"], self.group.id)
        self.assertEqual(response.data["gender"], TEST_GENDER)
        self.assertEqual(response.data["age"], TEST_AGE)

    def test_update_student(self):
        self.student_data["full_name"] = TEST_UPDATED_STUDENT_FULL_NAME
        response = self.client.put(path=self.detail_path, data=self.student_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TEST_UPDATED_STUDENT_FULL_NAME)

    def test_delete_group(self):
        response = self.client.delete(path=self.detail_path, follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
