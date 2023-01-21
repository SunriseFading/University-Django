from curator.permissions import IsCuratorUser
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from group.models import Group
from group.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser, IsCuratorUser]
