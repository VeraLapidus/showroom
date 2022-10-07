from django.db import models

from auto_show.models import AutoShow
from car.models import CarInstance
from customer.models import Customer
from producer.models import Producer


class Deal(models.Model):
    """ Сделки """

    name = models.CharField(max_length=200, blank=True, verbose_name="Название сделки")

    PARTICIPANTS = [('producer-showroom', 'поставщик-автосалон'), ('showroom-customer', 'автосалон-покупатель')]
    participants = models.CharField(max_length=40, choices=PARTICIPANTS, verbose_name='Стороны сделки')
    price = models.PositiveIntegerField(verbose_name='Сумма сделки, USD')

    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продавец")
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')
    car_instances = models.ForeignKey(CarInstance, on_delete=models.CASCADE, verbose_name='Авто')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата совершения сделки")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления сделки")

    class Meta:
        ordering = ['name']
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return self.name



