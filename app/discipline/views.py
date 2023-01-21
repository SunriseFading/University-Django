from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from discipline.models import Discipline
from discipline.serializers import DisciplineSerializer


class DisciplineListCreateView(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAdminUser]


class DisciplineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAdminUser]
