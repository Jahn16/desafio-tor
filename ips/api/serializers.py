from rest_framework.serializers import ModelSerializer
from ..models import Ip

class IpSerializer(ModelSerializer):
    class Meta:
        model = Ip
        fields = [
            'ip_address'
        ]
