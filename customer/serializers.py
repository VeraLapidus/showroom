from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer's data"""

    customers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'last_name', 'first_name', 'year_of_birth', 'balance', 'created', 'updated', 'is_active',
                  'customers']


class CustomerSerializerCreate(serializers.ModelSerializer):
    """Serializer for Customer's data (creating instances via api)"""

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'year_of_birth', 'balance', 'is_active']
