from curator.serializers import CuratorSerializer
from discipline.serializers import DisciplineSerializer
from rest_framework import serializers

from direction.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"
