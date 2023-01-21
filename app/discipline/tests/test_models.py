from account.models import CustomUser
from curator.models import Curator
from django.test import TestCase

from discipline.models import Discipline
from discipline.tests.settings import TEST_DISCIPLINE_NAME, TEST_UPDATED_DISCIPLINE_NAME


class DisciplineModelTestCase(TestCase):
    def setUp(self):
        self.discipline = Discipline.objects.create(name=TEST_DISCIPLINE_NAME)

    def test_create_discipline(self):
        self.assertEqual(Discipline.objects.count(), 1)

    def test_read_discipline(self):
        self.assertEqual(self.discipline.name, TEST_DISCIPLINE_NAME)

    def test_update_discipline(self):
        self.discipline.name = TEST_UPDATED_DISCIPLINE_NAME
        self.discipline.save()
        self.assertEqual(self.discipline.name, TEST_UPDATED_DISCIPLINE_NAME)

    def test_delete_discipline(self):
        self.discipline.delete()
        self.assertEqual(Discipline.objects.count(), 0)
