from rest_framework import serializers

from auto_show.serializers import AutoShowSerializer
from customer.serializers import CustomerSerializer
from producer.serializers import ProducerSerializer
from .models import Car, CarInstance


class CarSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по автомобилям """

    car_instances = serializers.StringRelatedField(many=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'description', 'created', 'updated', 'is_active', 'car_instances']


class CarInstanceSerializer(serializers.ModelSerializer):
    """  сериализатор для данных по экземплярам автомобилей """

    name = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    producers = serializers.SlugRelatedField(slug_field='name', read_only=True)
    auto_shows = serializers.SlugRelatedField(slug_field='name', read_only=True)
    customers = serializers.SlugRelatedField(slug_field='full_name', read_only=True)

    # name = CarSerializer(read_only=True)
    # producers = ProducerSerializer(read_only=True)
    # auto_shows = AutoShowSerializer(read_only=True)
    # customers = CustomerSerializer(read_only=True)

    class Meta:
        model = CarInstance
        fields = ['id', 'name', 'color', 'condition', 'customers', 'auto_shows', 'producers', 'price', 'created',
                  'updated', 'is_active']


class CarInstanceSerializerCreate(serializers.ModelSerializer):
    """  сериализатор для создания экземпляров автомобилей через api"""

    class Meta:
        model = CarInstance
        fields = ['name', 'color', 'condition', 'customers', 'auto_shows', 'producers', 'price', 'is_active']
