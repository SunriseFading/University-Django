# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIRequestFactory
# from rest_framework import status
# from curator.models import Curator
# from discipline.models import Discipline
# from direction.models import Direction
# from direction.views import DirectionListCreateView, DirectionRetrieveUpdateDestroyView
# from django.contrib.auth.models import Permission
# from account.models import CustomUser


# class DirectionViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = CustomUser.objects.create_superuser(
#             email="testadmin@example.com",
#             full_name="Test Admiin",
#             password="testpassword",
#             gender="male",
#             age=31
#         )
#         self.curator = Curator.objects.create(
#             email="testcurator@example.com",
#             full_name="Test Curator",
#             password="testpassword",
#             gender="male",
#             age=30,
#         )
#         self.discipline1 = Discipline.objects.create(name="Math")
#         self.discipline2 = Discipline.objects.create(name="Physics")
#         self.direction1 = Direction.objects.create(
#             name="Science",
#             curator=self.curator,
#         )
#         self.direction1.disciplines.set([self.discipline1, self.discipline2])
#         self.direction2 = Direction.objects.create(
#             name="Engineering",
#             curator=self.curator,
#         )
#         self.direction2.disciplines.set([self.discipline1])

#     def test_list_direction(self):
#         request = self.factory.get(reverse("direction:list"))
#         request.user = self.user
#         view = DirectionListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]["name"], "Science")
#         self.assertEqual(response.data[1]["name"], "Engineering")

#     def test_create_direction(self):
#         data = {
#             "name": "Arts",
#             "curator": self.curator.id,
#             "disciplines": [self.discipline1.id],
#         }
#         request = self.factory.post(reverse("direction:list"), data)
#         request.user = self.user
#         view = DirectionListCreateView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["name"], "Arts")

#     def test_retrieve_direction(self):
#         direction = Direction.objects.first()
#         request = self.factory.get(
#             reverse("direction:list", kwargs={"pk": direction.pk})
#         )
#         request.user = self.user
#         view = DirectionRetrieveUpdateDestroyView.as_view()
#         response = view(request, pk=1)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data["name"], "Science")

#     # def test_update_direction(self):
#     #     data = {'name': 'Sciences'}
