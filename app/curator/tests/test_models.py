from django.test import TestCase

from curator.models import Curator
from curator.tests.settings import (
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_CURATOR_FULL_NAME,
)


class CuratorModelTest(TestCase):
    def setUp(self):
        self.curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

    def test_create_curator(self):
        self.assertEqual(Curator.objects.count(), 1)

    def test_read_curator(self):
        self.assertEqual(self.curator.email, TEST_CURATOR_EMAIL)
        self.assertEqual(self.curator.full_name, TEST_CURATOR_FULL_NAME)
        self.assertEqual(self.curator.gender, TEST_GENDER)
        self.assertEqual(self.curator.age, TEST_AGE)

    def test_update_curator(self):
        self.curator.full_name = TEST_UPDATED_CURATOR_FULL_NAME
        self.curator.save()
        self.assertEqual(self.curator.full_name, TEST_UPDATED_CURATOR_FULL_NAME)

    def test_delete_curator(self):
        self.curator.delete()
        self.assertEqual(Curator.objects.count(), 0)
