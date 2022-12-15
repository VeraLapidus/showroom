import json

from celery import shared_task
from django.db.models import Q

from auto_show.models import AutoShow
from car.models import CarInstance
from deals.models import Deal
from producer.models import Producer


@shared_task
def sale_car_from_producer():
    # select one auto_show
    for auto_show in AutoShow.objects.all():

        # select auto_show's balance
        auto_show_balance = auto_show.balance

        # select auto_show's wish_car and transform it from TextField to list
        list_wish_car = auto_show.wish_car.split('  ')

        # create list_wish_car_after_search for removing the compared wish_car's element
        list_wish_car_after_search = list_wish_car

        # each wish_car from list_wish_car
        for elem_wish_car in list_wish_car:
            # make a dict from wish_car
            elem_wish_car_dict = json.loads(elem_wish_car)

            # select not empty dict's field for comparing with producer's cars
            dict_for_select = {}
            for key, value in elem_wish_car_dict.items():
                if key == 'brand' and value != "None":
                    dict_for_select['name__brand'] = value
                if key == 'model' and value != "None":
                    dict_for_select['name__model'] = value
                if key == 'year' and value != "None":
                    dict_for_select['name__year__gte'] = value
                if key == 'color' and value != "None":
                    dict_for_select['color'] = value
                if key == 'price' and value != "None":
                    dict_for_select['price__lte'] = value

            # select wish car from producer's cars
            if dict_for_select != {}:
                car = CarInstance.objects.filter(
                    Q(producers_id__isnull=False) & Q(price__lte=auto_show_balance)).filter(**dict_for_select).order_by(
                    'price').first()

                if car is not None:
                    # delete car from auto_show's wish_car
                    list_wish_car_after_search.remove(elem_wish_car)
                    str_wish_car = '  '.join(list_wish_car_after_search)

                    # decrease auto_show's balance
                    auto_show_balance = auto_show.balance - car.price
                    # increase producer's balance
                    producers_balance = car.producers.balance + car.price

                    # update CarInstance object
                    CarInstance.objects.filter(id=car.id).update(condition="At AutoShow", producers=None,
                                                                 auto_shows=auto_show)
                    # update AutoShow's object
                    AutoShow.objects.filter(id=auto_show.id).update(wish_car=str_wish_car, balance=auto_show_balance)
                    # update Producer's object
                    Producer.objects.filter(id=car.producers.id).update(balance=producers_balance)

                    # create new deal
                    Deal.objects.create(name=f'{car.name} from {car.producers.name} to {auto_show.name}',
                                        participants="Producer-AutoShow", producers=car.producers, auto_shows=auto_show,
                                        car_instances=car, price=car.price)
