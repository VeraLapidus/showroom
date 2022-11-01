from django_filters import rest_framework as filters

from .models import Deal


class DealFilter(filters.FilterSet):
    """  Фильтр-класс для модели сделки  """

    price = filters.RangeFilter()      #http://127.0.0.1:8000/api/deal/?price_max=100

    class Meta:
        model = Deal
        fields = ['price']
