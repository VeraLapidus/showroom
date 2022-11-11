from django_filters import rest_framework as filters

from car.models import Car, CarInstance


class CarFilter(filters.FilterSet):
    """Filter class for Car"""

    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['brand', 'model']


class CarInstanceFilter(filters.FilterSet):
    """Filter class for CarInstance"""

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = CarInstance
        fields = ['condition']
