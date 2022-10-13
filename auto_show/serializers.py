from rest_framework import serializers

from .models import AutoShow


class AutoShowSerializer(serializers.ModelSerializer):
    """ сериализатор для вывода всех автосалонов """

    class Meta:
        model = AutoShow
        fields = ['name', 'country', 'year_foundation', 'balance', 'wish_cars', 'list_auto', 'list_producers', 'list_customers',]
