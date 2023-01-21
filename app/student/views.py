from curator.permissions import IsCuratorUser
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from student.models import Student
from student.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser, IsCuratorUser]
