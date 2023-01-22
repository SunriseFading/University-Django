from curator.models import Curator
from direction.models import Direction
from django.test import TestCase

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


class GroupModelTest(TestCase):
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
        self.group = Group.objects.create(
            name=TEST_GROUP_NAME, direction=self.direction
        )

    def test_create_group(self):
        self.assertEqual(Group.objects.count(), 1)

    def test_read_group(self):
        self.assertEqual(self.group.name, TEST_GROUP_NAME)
        self.assertEqual(self.group.direction, self.direction)

    def test_update_group(self):
        self.group.name = TEST_UPDATED_GROUP_NAME
        self.group.save()
        self.assertEqual(self.group.name, TEST_UPDATED_GROUP_NAME)

    def test_delete_group(self):
        self.group.delete()
        self.assertEqual(Group.objects.count(), 0)
