from rest_framework import serializers

from deals.models import Deal


class DealSerializer(serializers.ModelSerializer):
    """  сериализатор для данных по сделкам """

    class Meta:
        model = Deal
        fields = '__all__'
