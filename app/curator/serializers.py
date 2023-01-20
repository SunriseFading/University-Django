from rest_framework import serializers
from curator.models import Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = (
            "id",
            "email",
            "full_name",
            "gender",
            "age",
            "is_active",
            "is_staff",
            "direction",
        )
