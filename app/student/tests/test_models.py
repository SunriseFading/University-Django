from curator.models import Curator
from direction.models import Direction
from django.test import TestCase
from group.models import Group

from student.models import Student
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


class StudentModelTest(TestCase):
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
        self.student = Student.objects.create(
            email=TEST_STUDENT_EMAIL,
            full_name=TEST_STUDENT_FULL_NAME,
            group=self.group,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

    def test_create_student(self):
        self.assertEqual(Student.objects.count(), 1)

    def test_read_student(self):
        self.assertEqual(self.student.email, TEST_STUDENT_EMAIL)
        self.assertEqual(self.student.full_name, TEST_STUDENT_FULL_NAME)
        self.assertEqual(self.student.group, self.group)
        self.assertEqual(self.student.gender, TEST_GENDER)
        self.assertEqual(self.student.age, TEST_AGE)

    def test_update_student(self):
        self.student.full_name = TEST_UPDATED_STUDENT_FULL_NAME
        self.student.save()
        self.assertEqual(self.student.full_name, TEST_UPDATED_STUDENT_FULL_NAME)

    def test_delete_student(self):
        self.student.delete()
        self.assertEqual(Student.objects.count(), 0)
