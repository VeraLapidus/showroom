from rest_framework import serializers

from .models import AutoShow


class AutoShowAllSerializer(serializers.ModelSerializer):
    """ сериализатор для основных данных по всем автосалонам """

    class Meta:
        model = AutoShow
        # fields = '__all__'
        fields = ['id', 'name', 'country', 'year_foundation', 'balance']


class AutoShowSerializer(serializers.ModelSerializer):
    """ сериализатор для детальной информации по одному автосалону """

    class Meta:
        model = AutoShow
        exclude = ['discount_producers', 'action_producers']
