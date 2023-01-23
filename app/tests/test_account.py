import pytest

from account.models import CustomUser
from django.urls import reverse
from rest_framework import status

from tests.settings import (
    TEST_AGE,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_USER_FULL_NAME,
    TEST_USER_EMAIL,
    TEST_USER_FULL_NAME,
    TEST_WRONG_PASSWORD,
)


@pytest.mark.django_db(transaction=True)
class TestUserView:
    login_path = reverse("account:login")
    login_data = {"email": TEST_USER_EMAIL, "password": TEST_PASSWORD}
    logout_path = reverse("account:logout")

    def test_login_success(self, client, user):
        response = client.post(path=self.login_path, data=self.login_data)
        assert response.status_code == status.HTTP_200_OK
        assert "token" in response.data

    def test_login_failure(self, client):
        self.login_data["password"] = TEST_WRONG_PASSWORD
        response = client.post(path=self.login_path, data=self.login_data)
        assert response.status_code, status.HTTP_400_BAD_REQUEST
        assert "error" in response.data

    def test_logout_success(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(path=self.logout_path)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db(transaction=True)
class UserManagerTest:
    def test_create_user(self, user):
        assert user.email == TEST_USER_EMAIL
        assert user.full_name == TEST_USER_FULL_NAME
        assert user.gender == TEST_GENDER
        assert user.age == TEST_AGE
        assert user.password != TEST_PASSWORD

    def test_create_superuser(self, superuser):
        assert superuser.is_superuser is True
        assert superuser.is_staff is True
        assert superuser.is_active is True


@pytest.mark.django_db(transaction=True)
class TestUserModel:
    def test_create_user(self, user):
        assert CustomUser.objects.count() == 1

    def test_read_user(self, user):
        assert user.email == TEST_USER_EMAIL
        assert user.full_name == TEST_USER_FULL_NAME
        assert user.gender == TEST_GENDER
        assert user.age == TEST_AGE
        assert user.password != TEST_PASSWORD

    def test_update_user(self, user):
        user.full_name = TEST_UPDATED_USER_FULL_NAME
        user.save()
        assert user.full_name == TEST_UPDATED_USER_FULL_NAME

    def test_delete_user(self, user):
        user.delete()
        assert CustomUser.objects.count() == 0
