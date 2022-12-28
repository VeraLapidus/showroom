from rest_framework import serializers

from producer.models import Producer
from user.serializers import UserSerializer


class ProducerSerializer(serializers.ModelSerializer):
    """Serializer for Producer's data"""

    producers = serializers.StringRelatedField(many=True)
    owner = UserSerializer()

    class Meta:
        model = Producer
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'amount_of_clients', 'created', 'updated',
                  'is_active', 'producers', 'owner']


class ProducerSerializerCreate(serializers.ModelSerializer):
    """Serializer for Producer's data (creating instances via api)"""

    class Meta:
        model = Producer
        fields = ['name', 'country', 'year_foundation', 'balance', 'is_active']
