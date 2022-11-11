from rest_framework import serializers

from auto_show.models import AutoShow


class AutoShowSerializer(serializers.ModelSerializer):
    """Serializer for AutoShow's data"""

    auto_shows = serializers.StringRelatedField(many=True)

    class Meta:
        model = AutoShow
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'wish_cars', 'list_auto', 'list_producers',
                  'list_customers', 'created', 'updated', 'is_active', 'auto_shows']


class AutoShowSerializerCreate(serializers.ModelSerializer):
    """Serializer for AutoShow's data (creating instances via api)"""

    class Meta:
        model = AutoShow
        fields = ['name', 'country', 'year_foundation', 'balance', 'wish_cars', 'is_active']
