from rest_framework import serializers

from auto_show.models import AutoShow
from user.serializers import UserSerializer


class AutoShowSerializer(serializers.ModelSerializer):
    """Serializer for AutoShow's data"""

    auto_shows = serializers.StringRelatedField(many=True)
    owner = UserSerializer()

    class Meta:
        model = AutoShow
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'wish_car', 'list_auto', 'list_producers',
                  'list_customers', 'created', 'updated', 'is_active', 'auto_shows', 'owner']


class AutoShowSerializerCreate(serializers.ModelSerializer):
    """Serializer for AutoShow's data (creating instances via api)"""

    class Meta:
        model = AutoShow
        fields = ['name', 'country', 'year_foundation', 'balance', 'wish_car', 'is_active']
