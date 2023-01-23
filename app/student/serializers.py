from account.serializers import CustomUserSerializer

from student.models import Student


class StudentSerializer(CustomUserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = Student
        fields = "__all__"
