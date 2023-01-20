from rest_framework import serializers
from student.models import Student
from group.serializers import GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Student
        fields = (
            "id",
            "email",
            "full_name",
            "gender",
            "age",
            "is_active",
            "is_staff",
            "group",
        )
