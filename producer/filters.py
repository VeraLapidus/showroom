from django_filters import rest_framework as filters

from .models import Producer


class ProducerFilter (filters.FilterSet):
    """ Фильтр-класс для модели производителя """

    class Meta:
        model = Producer
        fields = ['country', 'year_foundation']
