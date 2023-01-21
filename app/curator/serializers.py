from account.serializers import CustomUserSerializer

from curator.models import Curator


class CuratorSerializer(CustomUserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = Curator
