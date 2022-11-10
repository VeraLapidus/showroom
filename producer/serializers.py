from rest_framework import serializers

from producer.models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """Serializer for Producer's data"""

    producers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Producer
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'amount_of_clients', 'created', 'updated',
                  'is_active', 'producers']


class ProducerSerializerCreate(serializers.ModelSerializer):
    """Serializer for Producer's data (creating instances via api)"""

    class Meta:
        model = Producer
        fields = ['name', 'country', 'year_foundation', 'balance', 'is_active']
