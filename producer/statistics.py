from django.db.models import Sum, Q

from deals.enums import Participants
from deals.models import Deal
from deals.serializers import DealSerializer
from producer.models import Producer


def statistics(pk):
    producer = Producer.objects.get(pk=pk)
    queryset_for_statistics = Deal.objects.filter(
        Q(participants=Participants.PRODUCER_AUTOSHOW.value) & Q(producers=producer.id))
    amount_of_sold_cars = queryset_for_statistics.count()
    profit = queryset_for_statistics.aggregate(Sum('price'))['price__sum']

    # name and amount of unique clients
    unique_clients_list = []
    for deal in DealSerializer(queryset_for_statistics, many=True).data:
        unique_clients_list.append(deal.get("auto_shows"))
    unique_clients_set = set(unique_clients_list)
    amount_of_unique_clients = len(unique_clients_set)

    return {'producer_name': producer.name, 'amount_of_sold_cars': amount_of_sold_cars, 'profit': profit,
            'unique_clients': unique_clients_set, 'amount_of_unique_clients': amount_of_unique_clients}
