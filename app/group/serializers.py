from direction.serializers import DirectionSerializer
from rest_framework import serializers

from group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = Group
        fields = ("name", "direction", "number_students")
