from curator.permissions import IsCuratorUser
from group.models import Group
from rest_framework import generics, status
from rest_framework.response import Response

from student.models import Student
from student.serializers import StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorUser]

    def post(self, request, *args, **kwargs):
        group = Group.objects.get(id=request.data["group"])
        if group.students.count() >= 20:
            return Response(
                data={"error": "Group already have 20 students"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorUser]

    def put(self, request, *args, **kwargs):
        group = Group.objects.get(id=request.data["group"])
        if self.get_object().group != group and group.students.count() >= 20:
            return Response(
                data={"error": "Group already have 20 students"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        group = Group.objects.get(id=request.data["group"])
        if self.get_object().group != group and group.students.count() >= 20:
            return Response(
                data={"error": "Group already have 20 students"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return self.partial_update(request, *args, **kwargs)
