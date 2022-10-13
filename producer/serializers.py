from rest_framework import serializers

from .models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """ сериализатор для всех поставщиков """

    class Meta:
        model = Producer
        fields = ['name', 'country', 'year_foundation', 'balance', 'amount_of_clients',]