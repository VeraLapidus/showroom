from django_filters import rest_framework as filters

from producer.models import Producer


class ProducerFilter(filters.FilterSet):
    """Filter class for Producer"""

    year_foundation = filters.RangeFilter()

    class Meta:
        model = Producer
        fields = ['country', 'year_foundation']
