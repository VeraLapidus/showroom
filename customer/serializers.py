from rest_framework import serializers

from .models import Customer


class CustomerAllSerializer(serializers.ModelSerializer):
    """ сериализатор для вывода всех клиентов """

    class Meta:
        model = Customer
        fields = ['id', 'last_name', 'first_name', 'year_of_birth', 'balance']


class CustomerSerializer(serializers.ModelSerializer):
    """ сериализатор для детальной информации по одному клиенту """

    class Meta:
        model = Customer
        fields = '__all__'