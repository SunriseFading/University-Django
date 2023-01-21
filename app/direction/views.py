from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from direction.models import Direction
from direction.serializers import DirectionSerializer


class DirectionListCreateView(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminUser]


class DirectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminUser]
