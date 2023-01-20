from rest_framework import serializers
from curator.serializers import CuratorSerializer
from direction.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    disciplines = serializers.StringRelatedField(many=True)
    curator = CuratorSerializer()

    class Meta:
        model = Direction
        fields = ("id", "name", "curator", "disciplines", "groups")
