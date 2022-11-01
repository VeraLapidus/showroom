from django_filters import rest_framework as filters

from .models import AutoShow


class AutoShowFilter(filters.FilterSet):
    """ Фильтр-класс для модели автосалона """

    class Meta:
        model = AutoShow
        fields = ['country', 'year_foundation']
