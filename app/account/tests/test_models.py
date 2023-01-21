from django.test import TestCase

from account.models import CustomUser
from account.tests.settings import (
    TEST_EMAIL,
    TEST_FULL_NAME,
    TEST_PASSWORD,
    TEST_AGE,
    TEST_GENDER,
)


class UserManagerTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )

        self.assertEqual(user.email, TEST_EMAIL)
        self.assertEqual(user.full_name, TEST_FULL_NAME)
        self.assertEqual(user.gender, TEST_GENDER)
        self.assertEqual(user.age, TEST_AGE)
        self.assertNotEqual(user.password, TEST_PASSWORD)

    def test_create_user_missing_email(self):
        with self.assertRaises(ValueError) as error:
            CustomUser.objects.create_user(
                email=None,
                full_name=TEST_FULL_NAME,
                gender=TEST_GENDER,
                age=TEST_AGE,
                password=TEST_PASSWORD,
            )
        self.assertEqual(str(error.exception), "User must have email")

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser_missing_permissions(self):
        with self.assertRaises(ValueError) as error:
            CustomUser.objects.create_superuser(
                email=TEST_EMAIL,
                full_name=TEST_FULL_NAME,
                gender=TEST_GENDER,
                age=TEST_AGE,
                password=TEST_PASSWORD,
                is_staff=False,
            )
        self.assertEqual(
            str(error.exception), "Superuser must be assigned to is_staff=True"
        )


class UserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        user.save()

        saved_user = CustomUser.objects.first()
        self.assertEqual(saved_user.email, TEST_EMAIL)
        self.assertEqual(saved_user.full_name, TEST_FULL_NAME)

    def test_user_string_representation(self):
        user = CustomUser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        user.save()

        self.assertEqual(str(user), TEST_EMAIL)

    def test_user_verbose_name(self):
        self.assertEqual(str(CustomUser._meta.verbose_name), "Пользователь")
        self.assertEqual(str(CustomUser._meta.verbose_name_plural), "Пользователи")

    def test_user_permissions(self):
        user = CustomUser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        user.save()

        self.assertFalse(user.has_perm("add_user"))
        self.assertFalse(user.has_perm("delete_user"))

    def test_user_is_active(self):
        user = CustomUser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        user.save()

        self.assertTrue(user.is_active)

    def test_user_is_staff(self):
        user = CustomUser(
            email=TEST_EMAIL,
            full_name=TEST_FULL_NAME,
            gender=TEST_GENDER,
            age=TEST_AGE,
            password=TEST_PASSWORD,
        )
        user.save()

        self.assertFalse(user.is_staff)

        user.is_staff = True
        user.save()

        self.assertTrue(user.is_staff)
