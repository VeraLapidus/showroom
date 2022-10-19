from rest_framework import serializers

from .models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по поставщикам """

    class Meta:
        model = Producer
        fields = '__all__'

