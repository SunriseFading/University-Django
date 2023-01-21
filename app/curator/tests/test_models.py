from account.models import CustomUser
from django.test import TestCase

from curator.models import Curator
from curator.tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_AGE,
    TEST_GENDER,
    TEST_PASSWORD,
)


class CuratorModelTestCase(TestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser(
            email=TEST_ADMIN_EMAIL,
            full_name=TEST_ADMIN_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

    def test_create_curator(self):
        curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.assertEqual(curator.email, TEST_CURATOR_EMAIL)

    def test_read_curator(self):
        curator = Curator.objects.create(
            email=TEST_CURATOR_EMAIL,
            full_name=TEST_CURATOR_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.assertEqual(curator.full_name, TEST_CURATOR_FULL_NAME)
