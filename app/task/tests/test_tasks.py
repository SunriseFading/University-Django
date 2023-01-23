import os

from curator.models import Curator
from direction.models import Direction
from discipline.models import Discipline
from group.models import Group
from rest_framework.test import APITestCase
from student.models import Student

from task.tasks import create_report

from task.tests.settings import TEST_AGE, TEST_CURATOR_FULL_NAME, TEST_GENDER, TEST_PASSWORD, TEST_STUDENT_FULL_NAME


class TaskReportTest(APITestCase):
    def setUp(self):
        for i in range(3):
            curator = Curator.objects.create(
                email=f"curator{i}@test.com",
                full_name=TEST_CURATOR_FULL_NAME,
                gender=TEST_GENDER,
                age=TEST_AGE,
                password=TEST_PASSWORD,
            )
            direction = Direction.objects.create(name=f"Direction {i}", curator=curator)
            for j in range(3):
                discipline = Discipline.objects.create(name=f"Discipline {i}{j}")
                direction.disciplines.add(discipline)

            group = Group.objects.create(name=f"Group {i}", direction=direction)
            for j in range(3):
                Student.objects.create(
                    email=f"student{i}{j}@test.com",
                    full_name=TEST_STUDENT_FULL_NAME,
                    group=group,
                    gender=TEST_GENDER,
                    age=TEST_AGE,
                    password=TEST_PASSWORD,
                )

    def test_create_report(self):
        directions = Direction.objects.all()
        groups = Group.objects.all()
        students = Student.objects.all()
        create_report(directions=directions, groups=groups, students=students)
        self.assertTrue(os.path.exists("media/report.xlsx"))
