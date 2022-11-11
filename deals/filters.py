from django_filters import rest_framework as filters

from deals.models import Deal


class DealFilter(filters.FilterSet):
    """Filter class for Deal"""

    price = filters.RangeFilter()

    class Meta:
        model = Deal
        fields = ['price']
