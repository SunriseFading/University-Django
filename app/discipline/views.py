from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from discipline.models import Discipline
from discipline.serializers import DisciplineSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAdminUser]
