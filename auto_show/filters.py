from django_filters import rest_framework as filters

from auto_show.models import AutoShow


class AutoShowFilter(filters.FilterSet):
    """Filter class for AutoShow"""

    year_foundation = filters.RangeFilter()

    class Meta:
        model = AutoShow
        fields = ['country', 'year_foundation']
