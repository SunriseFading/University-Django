import pytest
from account.models import CustomUser
from curator.models import Curator
from direction.models import Direction
from discipline.models import Discipline
from django.conf import settings
from django.urls import reverse
from group.models import Group
from rest_framework.test import APIClient
from student.models import Student

from tests.settings import (
    TEST_ADMIN_EMAIL,
    TEST_ADMIN_FULL_NAME,
    TEST_AGE,
    TEST_CURATOR_EMAIL,
    TEST_CURATOR_FULL_NAME,
    TEST_GENDER,
    TEST_PASSWORD,
    TEST_STUDENT_FULL_NAME,
    TEST_USER_EMAIL,
    TEST_USER_FULL_NAME,
)

curator_data = {
    "email": TEST_CURATOR_EMAIL,
    "full_name": TEST_CURATOR_FULL_NAME,
    "gender": TEST_GENDER,
    "age": TEST_AGE,
    "password": TEST_PASSWORD,
}


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"]


@pytest.mark.django_db
@pytest.fixture()
def user():
    return CustomUser.objects.create_user(
        email=TEST_USER_EMAIL, password=TEST_PASSWORD, full_name=TEST_USER_FULL_NAME, gender=TEST_GENDER, age=TEST_AGE
    )


@pytest.mark.django_db
@pytest.fixture()
def superuser():
    return CustomUser.objects.create_superuser(
        email=TEST_ADMIN_EMAIL, full_name=TEST_ADMIN_FULL_NAME, gender=TEST_GENDER, age=TEST_AGE, password=TEST_PASSWORD
    )


@pytest.mark.django_db
@pytest.fixture()
def curator():
    return Curator.objects.create(
        email=TEST_CURATOR_EMAIL,
        full_name=TEST_CURATOR_FULL_NAME,
        gender=TEST_GENDER,
        age=TEST_AGE,
        password=TEST_PASSWORD,
    )


@pytest.mark.django_db
@pytest.fixture()
def fake_date():
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


@pytest.fixture
def detail_path(auth_superuser):
    curator_data = {
        "email": TEST_CURATOR_EMAIL,
        "full_name": TEST_CURATOR_FULL_NAME,
        "gender": TEST_GENDER,
        "age": TEST_AGE,
        "password": TEST_PASSWORD,
    }
    response = auth_superuser.post(reverse("curator:list"), data=curator_data)
    return reverse("curator:detail", kwargs={"pk": response.json()["id"]})


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_superuser(client: APIClient, superuser: CustomUser):
    client.force_authenticate(user=superuser)
    return client


@pytest.fixture
def auth_curator(client: APIClient, curator: CustomUser):
    client.force_authenticate(user=curator)
    return client


@pytest.fixture
def detail_curator_path(auth_superuser: APIClient):
    response = auth_superuser.post(path=reverse("curator:list"), data=curator_data)
    return reverse("curator:detail", args=response.json()["id"])
