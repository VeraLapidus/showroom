from rest_framework import serializers

from .models import Car, CarInstance


class CarAllSerializer(serializers.ModelSerializer):
    """ сериализатор для основных данных по всем автомобилям """

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'description']


class CarSerializer(serializers.ModelSerializer):
    """ сериализатор для детальной информации по одному автомобилю """

    class Meta:
        model = Car
        fields = '__all__'


class CarInstanceAllSerializer (serializers.ModelSerializer):
    """  сериализатор для основных данных по всем экземплярам автомобилей """
    class Meta:
        model = CarInstance
        fields = ['id', 'name', 'color', 'condition', 'price']