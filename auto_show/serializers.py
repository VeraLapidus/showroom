from rest_framework import serializers

from .models import AutoShow


class AutoShowSerializer(serializers.ModelSerializer):
    """ сериализатор данных автосалона """

    class Meta:
        model = AutoShow
        fields = '__all__'

