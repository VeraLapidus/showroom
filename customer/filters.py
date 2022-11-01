from django_filters import rest_framework as filters

from .models import Customer


class CustomerFilter(filters.FilterSet):
    """ Фильтр-класс для модели клиента """

    min_balance = filters.NumberFilter(field_name="balance", lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name="balance", lookup_expr='lte')

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'balance']
