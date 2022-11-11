from django.db import models

from additional.enums import Participants
from additional.models import BaseData
from auto_show.models import AutoShow
from car.models import CarInstance
from customer.models import Customer
from producer.models import Producer


class Deal(BaseData):
    """Model for Deal"""

    name = models.CharField(max_length=200, blank=True, verbose_name="Название сделки")
    participants = models.CharField(max_length=50, choices=Participants.choices(), verbose_name='Стороны сделки')
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Поставщик")
    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')
    car_instances = models.ForeignKey(CarInstance, on_delete=models.CASCADE, verbose_name='Авто')
    price = models.PositiveIntegerField(verbose_name='Сумма сделки, USD')

    class Meta:
        ordering = ['name']
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return self.name
