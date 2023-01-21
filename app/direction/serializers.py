from curator.serializers import CuratorSerializer
from discipline.serializers import DisciplineSerializer
from rest_framework import serializers

from direction.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    curator = CuratorSerializer()
    disciplines = DisciplineSerializer(many=True)

    class Meta:
        model = Direction
        fields = ('name', 'curator', 'disciplines')
