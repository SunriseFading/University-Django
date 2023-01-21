from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from curator.models import Curator
from curator.serializers import CuratorSerializer


class CuratorListCreateView(generics.ListCreateAPIView):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminUser]


class CuratorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminUser]
