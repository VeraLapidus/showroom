from django_filters import rest_framework as filters

from .models import Car, CarInstance


class CarFilter(filters.FilterSet):
    """  Фильтр-класс для модели автомобилей """

    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['brand', 'model', 'year']


class CarInstanceFilter(filters.FilterSet):
    """  Фильтр-класс для модели экземпляров автомобиля """

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = CarInstance
        fields = ['condition', 'price']
