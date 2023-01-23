import pytest

from curator.models import Curator
from django.urls import reverse
from rest_framework import status

from tests.settings import (
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_UPDATED_CURATOR_FULL_NAME,
)


@pytest.mark.django_db(transaction=True)
class TestCuratorView:
    curator_data = {
        "email": TEST_CURATOR_EMAIL,
        "full_name": TEST_CURATOR_FULL_NAME,
        "gender": TEST_GENDER,
        "age": TEST_AGE,
        "password": TEST_PASSWORD,
    }
    list_path = reverse("curator:list")

    def test_create_curator(self, auth_superuser):
        response = auth_superuser.post(path=self.list_path, data=self.curator_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_read_curator(self, auth_superuser, detail_path):
        response = auth_superuser.get(path=detail_path)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert response.get("email") == TEST_CURATOR_EMAIL
        assert response.get("full_name") == TEST_CURATOR_FULL_NAME
        assert response.get("gender") == TEST_GENDER
        assert response.get("age") == TEST_AGE

    def test_list_curators(self, auth_superuser, detail_path):
        response = auth_superuser.get(path=self.list_path)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_update_curator(self, auth_superuser, detail_path):
        self.curator_data["full_name"] = TEST_UPDATED_CURATOR_FULL_NAME
        response = auth_superuser.put(path=detail_path, data=self.curator_data)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert response.get("full_name") == TEST_UPDATED_CURATOR_FULL_NAME

    def test_delete_curator(self, auth_superuser, detail_path):
        response = auth_superuser.delete(path=detail_path, follow=True)
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db(transaction=True)
class TestCuratorModel:
    def test_create_curator(self, curator):
        assert Curator.objects.count() == 1

    def test_read_curator(self, curator):
        assert curator.email == TEST_CURATOR_EMAIL
        assert curator.full_name == TEST_CURATOR_FULL_NAME
        assert curator.gender == TEST_GENDER
        assert curator.age == TEST_AGE

    def test_update_curator(self, curator):
        curator.full_name = TEST_UPDATED_CURATOR_FULL_NAME
        curator.save()
        assert curator.full_name == TEST_UPDATED_CURATOR_FULL_NAME

    def test_delete_curator(self, curator):
        curator.delete()
        assert Curator.objects.count() == 0
