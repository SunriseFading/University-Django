from django.test import TestCase

from account.models import CustomUser
from account.tests.settings import (
    TEST_AGE,
    TEST_USER_EMAIL,
    TEST_USER_FULL_NAME,
    TEST_UPDATED_USER_FULL_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
)


class UserManagerTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email=TEST_USER_EMAIL,
            full_name=TEST_USER_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

        self.assertEqual(user.email, TEST_USER_EMAIL)
        self.assertEqual(user.full_name, TEST_USER_FULL_NAME)
        self.assertEqual(user.gender, TEST_GENDER)
        self.assertEqual(user.age, TEST_AGE)
        self.assertNotEqual(user.password, TEST_PASSWORD)

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email=TEST_USER_EMAIL,
            full_name=TEST_USER_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email=TEST_USER_EMAIL,
            full_name=TEST_USER_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

    def test_create_user(self):
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_read_user(self):
        self.assertEqual(self.user.email, TEST_USER_EMAIL)
        self.assertEqual(self.user.full_name, TEST_USER_FULL_NAME)
        self.assertEqual(self.user.gender, TEST_GENDER)
        self.assertEqual(self.user.age, TEST_AGE)
        self.assertNotEqual(self.user.password, TEST_PASSWORD)

    def test_update_user(self):
        self.user.full_name = TEST_UPDATED_USER_FULL_NAME
        self.user.save()
        self.assertEqual(self.user.full_name, TEST_UPDATED_USER_FULL_NAME)

    def test_delete_user(self):
        self.user.delete()
        self.assertEqual(CustomUser.objects.count(), 0)
