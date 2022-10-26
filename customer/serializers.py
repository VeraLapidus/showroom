from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по клиентам """

    customers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'year_of_birth', 'balance', 'created', 'updated', 'is_active', 'customers']


class CustomerSerializerCreate(serializers.ModelSerializer):
    """ сериализатор для создания клиента через api """

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'year_of_birth', 'balance', 'is_active']