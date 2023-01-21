from rest_framework import serializers

from account.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "full_name", "gender", "age", "password")
