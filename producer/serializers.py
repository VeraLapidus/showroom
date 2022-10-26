from rest_framework import serializers

from .models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по поставщикам """

    producers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Producer
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'amount_of_clients', 'created', 'updated',
                  'is_active', 'producers']


class ProducerSerializerCreate(serializers.ModelSerializer):
    """ сериализатор для создания поставщика """

    class Meta:
        model = Producer
        fields = ['name', 'country', 'year_foundation', 'balance', 'is_active']
