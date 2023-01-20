from rest_framework import serializers
from discipline.models import Discipline

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id','name')