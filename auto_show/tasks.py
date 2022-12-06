import json

from celery import shared_task

from auto_show.models import AutoShow
from car.models import CarInstance
from deals.models import Deal
from producer.models import Producer


@shared_task
def sale_car_from_producer():
    """ Функция, которая ищет наличие авто из wish_car автосалона у поставщика;
      При наличии такого авто у поставщика (и выполнении ряда проверок):
       - если таких авто у поставщика несколько, но цена разная - выбирает авто с мин ценой;
       - происходит покупка авто:
           -- статус CarInstance меняется с AT_PRODUCER на AT_AUTOSHOW, заполняется поле 'producers', поле 'auto_shows'= None
           -- у AutoShow из поля 'wish_car' удаляется купленное авто, уменьшается баланс
           -- у Producer увеличивается баланс
           -- создается экземпляр модели Deal   """

    auto_shows = AutoShow.objects.all()
    for auto_show in auto_shows:
        auto_show_balance = auto_show.balance
        str_wish_car = auto_show.wish_car
        list_wish_car = str_wish_car.split('  ')
        for j in list_wish_car:
            b = json.loads(j)  # получили dict каждой машины из wish_car
            brand_wish_showroom = b.get("brand")
            model_wish_showroom = b.get("model")
            price_wish_car = b.get("price")

            if price_wish_car != "None" and price_wish_car is not None:
                price_wish_car_int = int(price_wish_car)
                cars = CarInstance.objects.filter(producers_id__isnull=False, name__brand=brand_wish_showroom,
                                                  name__model=model_wish_showroom,
                                                  price__lte=price_wish_car_int).filter(
                    price__lte=auto_show_balance).order_by('price')[0:1]
                # получили queryset (авто у поставщика, price - min, если одинаковых авто несколько),
                # соответсвующих машине из wish_car
                for car in cars:
                    list_wish_car.remove(j)
                    str_wish_car = '  '.join(list_wish_car)  # удаляем покупаемую машину из wish_list автосалона
                    auto_show_balance = auto_show.balance - car.price  # уменьшаем баланс автосалона
                    producers_balance = car.producers.balance + car.price  # увеличиваем баланс производителя

                    updated_car_instance = CarInstance.objects.filter(id=car.id).update(condition="В автосалоне",
                                                                                        producers=None,
                                                                                        auto_shows=auto_show)
                    updated_auto_show = AutoShow.objects.filter(id=auto_show.id).update(wish_car=str_wish_car,
                                                                                        balance=auto_show_balance)
                    updated_producer = Producer.objects.filter(id=car.producers.id).update(balance=producers_balance)
                    new_deal = Deal(name=f'{car.name} from {car.producers.name} to {auto_show.name}',
                                    participants="Поставщик-автосалон", producers=car.producers, auto_shows=auto_show,
                                    car_instances=car, price=car.price)
                    new_deal.save()
                    print('SAVE')
