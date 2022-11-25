import json

from celery import shared_task

from auto_show.models import AutoShow
from car.models import CarInstance
from deals.models import Deal
from producer.models import Producer


@shared_task
def sale_car_from_producer():
    auto_shows = AutoShow.objects.all()
    carinstance = CarInstance.objects.all()
    for auto_show in auto_shows:
        str_wish_car = auto_show.wish_car
        list_wish_car = str_wish_car.split('  ')
        for j in list_wish_car:
            b = json.loads(j)  # получили dict
            brand_wish_showroom = b.get("brand")
            model_wish_showroom = b.get("model")
            price_wish_car = b.get("price")
            for t in carinstance:
                carinstance_id = t.id
                if t.producers_id is not None:
                    if t.name.brand == brand_wish_showroom and t.name.model == model_wish_showroom:  # сверяем бренд и модель автомобилей из wish_list автосалона и производителя
                        if type(price_wish_car) == str:
                            if t.price <= int(price_wish_car) and auto_show.balance >= t.price:
                                list_wish_car.remove(j)
                                str_wish_car = '  '.join(
                                    list_wish_car)  # удаляем покупаемую машину из wish_list автосалона
                                auto_show_balance = auto_show.balance - t.price  # уменьшаем баланс автосалона
                                producers_balance = t.producers.balance + t.price  # увеличиваем баланс производителя

                                updated_car_instance = CarInstance.objects.filter(id=carinstance_id).update(
                                    condition="В автосалоне", producers=None, auto_shows=auto_show)
                                updated_auto_show = AutoShow.objects.filter(id=auto_show.id).update(
                                    wish_car=str_wish_car, balance=auto_show_balance)
                                updated_producer = Producer.objects.filter(id=t.producers.id).update(
                                    balance=producers_balance)
                                new_deal = Deal(name=f'{t.name} from {t.producers.name} to {auto_show.name}',
                                                participants="Поставщик-автосалон", producers=t.producers,
                                                auto_shows=auto_show, car_instances=t, price=t.price)
                                new_deal.save()
                                print('SAVE')
