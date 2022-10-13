from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """ сериализатор для вывода всех автомобилей """

    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'description',]
