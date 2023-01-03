from django.db.models import Q, Sum
from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from deals.models import Deal
from deals.serializers import DealSerializer
from producer.filters import ProducerFilter
from producer.models import Producer
from producer.serializers import ProducerSerializer, ProducerSerializerCreate


class ProducerViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProducerFilter

    @action(methods=['get'], detail=True)
    def statistics(self, request, pk=None):
        producer = Producer.objects.get(pk=pk)
        queryset_for_statistics = Deal.objects.filter(Q(participants="Producer-AutoShow") & Q(producers=producer.id))
        amount_of_sold_cars = queryset_for_statistics.count()
        profit = queryset_for_statistics.aggregate(Sum('price'))['price__sum']

        # name and amount of unique clients
        unique_clients_list = []
        for deal in DealSerializer(queryset_for_statistics, many=True).data:
            unique_clients_list.append(deal.get("auto_shows"))
        unique_clients_set = set(unique_clients_list)
        amount_of_unique_clients = len(unique_clients_set)

        context = {'producer_name': producer.name, 'amount_of_sold_cars': amount_of_sold_cars, 'profit': profit,
                   'unique_clients': unique_clients_set, 'amount_of_unique_clients': amount_of_unique_clients}
        return Response(context)


def get_serializer_class(self, *args, **kwargs):
    if self.request.method == "POST":
        return ProducerSerializerCreate

    return self.serializer_class
