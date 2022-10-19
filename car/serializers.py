from rest_framework import serializers

from .models import Car, CarInstance


class CarSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по автомобилям """

    class Meta:
        model = Car
        fields = '__all__'


class CarInstanceSerializer(serializers.ModelSerializer):
    """  сериализатор для данных по экземплярам автомобилей """

    class Meta:
        model = CarInstance
        fields = '__all__'
