from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """ сериализатор для вывода всех клиентов """

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'year_of_birth', 'balance',]
