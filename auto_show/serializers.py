from rest_framework import serializers

from .models import AutoShow


class AutoShowSerializer(serializers.ModelSerializer):
    """ сериализатор данных автосалона """

    auto_shows = serializers.StringRelatedField(many=True)

    class Meta:
        model = AutoShow
        fields = ['id', 'name', 'country', 'year_foundation', 'balance', 'wish_cars', 'list_auto', 'list_producers',
                  'list_customers', 'created', 'updated', 'is_active', 'auto_shows']


class AutoShowSerializerCreate(serializers.ModelSerializer):
    """ сериализатор данных автосалона для создания через api"""

    class Meta:
        model = AutoShow
        fields = ['name', 'country', 'year_foundation', 'balance', 'wish_cars', 'is_active']
