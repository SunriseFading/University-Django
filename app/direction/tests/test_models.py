from account.models import CustomUser
from curator.models import Curator
from discipline.models import Discipline
from django.test import TestCase

from direction.models import Direction
from direction.tests.settings import (
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_DIRECTION_NAME,
    TEST_UPDATED_DIRECTION_NAME,
    TEST_DISCIPLINE_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
)


class DirectionModelTest(TestCase):
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
        self.discipline = Discipline.objects.create(name=TEST_DISCIPLINE_NAME)
        self.direction.disciplines.add(self.discipline)

    def test_create_direction(self):
        self.assertEqual(Direction.objects.count(), 1)

    def test_read_direction(self):
        self.assertEqual(self.direction.name, TEST_DIRECTION_NAME)
        self.assertEqual(self.direction.curator, self.curator)
        self.assertEqual(self.direction.disciplines.all()[0], self.discipline)

    def test_update_direction(self):
        self.direction.name = TEST_UPDATED_DIRECTION_NAME
        self.direction.save()
        self.assertEqual(self.direction.name, TEST_UPDATED_DIRECTION_NAME)

    def test_delete_direction(self):
        self.direction.delete()
        self.assertEqual(Direction.objects.count(), 0)
