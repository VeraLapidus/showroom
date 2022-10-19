from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """ сериализатор для данных по клиентам """

    class Meta:
        model = Customer
        fields = '__all__'