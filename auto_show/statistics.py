from django.db.models import Sum, Q

from auto_show.models import AutoShow
from deals.models import Deal
from deals.serializers import DealSerializer


def statistics(pk):
    auto_show = AutoShow.objects.get(pk=pk)
    queryset_for_statistics = Deal.objects.filter(Q(participants="Producer-AutoShow") & Q(auto_shows=auto_show.id))
    amount_of_bought_cars = queryset_for_statistics.count()
    consumption = queryset_for_statistics.aggregate(Sum('price'))['price__sum']

    # bought_cars
    bought_cars = []
    for deal in DealSerializer(queryset_for_statistics, many=True).data:
        bought_cars.append(deal.get("car_instances"))

    return {'auto_show': auto_show.name, 'amount_of_bought_cars': amount_of_bought_cars,
            'consumption, USD': consumption, 'bought_cars': bought_cars}
