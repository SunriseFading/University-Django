from rest_framework import serializers
from direction.serializers import DirectionSerializer
from student.serializers import StudentSerializer
from group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = Group
        fields = ("id", "name", "direction", "number_students")
