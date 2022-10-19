from rest_framework import serializers

from .models import Producer


class ProducerAllSerializer(serializers.ModelSerializer):
    """ сериализатор для основных данных по всем поставщикам """

    class Meta:
        model = Producer
        fields = ['id', 'name', 'country', 'year_foundation', 'balance']

class ProducerSerializer(serializers.ModelSerializer):
    """ сериализатор для детальной информации по одному поставщику """

    class Meta:
        model = Producer
        fields = '__all__'