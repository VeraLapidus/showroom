from rest_framework import filters
from django_filters import rest_framework
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .filters import DealFilter
from .models import Deal
from .serializers import DealSerializer


class DealViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных для сделок """

    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = DealFilter
    search_fields = ['producers__name', 'auto_shows__name', 'customers__last_name', 'car_instances__name__brand']
    ordering_fields = ['price', 'id']          #http://127.0.0.1:8000/deal/?ordering=-price

