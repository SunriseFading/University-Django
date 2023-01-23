import os

import pytest

from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestTaskReport:
    def test_create_report(self, auth_superuser, fake_date):
        create_report_path = reverse("task:create_report")
        response = auth_superuser.post(path=create_report_path)
        retrive_report_path = reverse("task:retrive_report", kwargs={"task_id": response.json()["task_id"]})
        auth_superuser.get(path=retrive_report_path)
        assert os.path.exists("../media/report.xlsx") is True
