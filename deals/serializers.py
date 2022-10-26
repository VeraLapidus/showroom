from rest_framework import serializers

from car.serializers import CarInstanceSerializer
from deals.models import Deal


class DealSerializer(serializers.ModelSerializer):
    """  сериализатор для данных по сделкам """

    car_instances = CarInstanceSerializer(read_only=True)
    producers = serializers.SlugRelatedField(slug_field='name', read_only=True)
    auto_shows = serializers.SlugRelatedField(slug_field='name', read_only=True)
    customers = serializers.SlugRelatedField(slug_field='full_name', read_only=True)


    class Meta:
        model = Deal
        fields = ['id', 'name', 'participants', 'producers',  'auto_shows',  'customers', 'price', 'car_instances',
                  'created', 'updated', 'is_active']
