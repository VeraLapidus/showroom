from django.db.models import Q, Sum

from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from auto_show.filters import AutoShowFilter
from auto_show.models import AutoShow
from auto_show.serializers import AutoShowSerializer, AutoShowSerializerCreate
from deals.models import Deal
from deals.serializers import DealSerializer


class AutoShowViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    queryset = AutoShow.objects.all()
    serializer_class = AutoShowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AutoShowFilter

    @action(methods=['get'], detail=True)
    def statistics(self, request, pk=None):
        auto_show = AutoShow.objects.get(pk=pk)
        queryset_for_statistics = Deal.objects.filter(Q(participants="Producer-AutoShow") & Q(auto_shows=auto_show.id))
        amount_of_bought_cars = queryset_for_statistics.count()
        consumption = queryset_for_statistics.aggregate(Sum('price'))['price__sum']

        # bought_cars
        bought_cars = []
        for deal in DealSerializer(queryset_for_statistics, many=True).data:
            bought_cars.append(deal.get("car_instances"))

        context = {'auto_show': auto_show.name, 'amount_of_bought_cars': amount_of_bought_cars,
                   'consumption, USD': consumption, 'bought_cars': bought_cars}
        return Response(context)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return AutoShowSerializerCreate

        return self.serializer_class
