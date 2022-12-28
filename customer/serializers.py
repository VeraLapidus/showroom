from rest_framework import serializers

from customer.models import Customer
from user.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer's data"""

    customers = serializers.StringRelatedField(many=True)
    owner = UserSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'last_name', 'first_name', 'year_of_birth', 'balance', 'wish_car', 'created', 'updated',
                  'is_active', 'customers', 'owner']


class CustomerSerializerCreate(serializers.ModelSerializer):
    """Serializer for Customer's data (creating instances via api)"""

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'year_of_birth', 'balance', 'wish_car', 'is_active']
