import json

from celery import shared_task

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

        # select fields for comparing
        for elem in list_wish_car:
            b = json.loads(elem)
            brand_wish_car = b.get("brand")
            model_wish_car = b.get("model")
            price_wish_car = b.get("price")

            # check price
            if price_wish_car != "None" and price_wish_car is not None:
                price_wish_car_int = int(price_wish_car)

                # choose car with min price (order_by('price')[0])
                ### обернуть конструкцию try-exept плюс параметры передавать через filtr params и ** и добавить Q объекты
                car = CarInstance.objects.filter(producers_id__isnull=False, name__brand=brand_wish_car,
                                                 name__model=model_wish_car, price__lte=price_wish_car_int).filter(
                    price__lte=auto_show_balance).order_by('price')[0]

                # delete car from auto_show's wish_car
                list_wish_car.remove(elem)
                str_wish_car = '  '.join(list_wish_car)

                # decrease auto_show's balance
                auto_show_balance = auto_show.balance - car.price
                # increase producer's balance
                producers_balance = car.producers.balance + car.price

                # change car's status
                CarInstance.objects.filter(id=car.id).update(status="At AutoShow", producers=None,
                                                             auto_shows=auto_show)
                # change auto_show's status
                AutoShow.objects.filter(id=auto_show.id).update(wish_car=str_wish_car, balance=auto_show_balance)
                # change producer's status
                Producer.objects.filter(id=car.producers.id).update(balance=producers_balance)

                # create new deal
                Deal.objects.create(name=f'{car.name} from {car.producers.name} to {auto_show.name}',
                                    participants="Producer-AutoShow", producers=car.producers, auto_shows=auto_show,
                                    car_instances=car, price=car.price)
