from django.db import models

from abstract.abstract_models import BaseData
from auto_show.models import AutoShow
from car.enums import CarStatus
from producer.models import Producer
from customer.models import Customer


class Car(BaseData):
    brand = models.CharField(max_length=50, verbose_name="Бренд")
    model = models.CharField(max_length=50, verbose_name=" Mодель")
    year = models.CharField(max_length=4, verbose_name="Год выпуска")
    description = models.TextField(blank=True, verbose_name='Описание')

    @property
    def full_name(self):
        return "{} {} {}".format(self.brand, self.model, self.year)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class CarInstance(BaseData):
    name = models.ForeignKey(Car, related_name='car_instances', on_delete=models.CASCADE, verbose_name="Автомобиль")
    color = models.CharField(max_length=200, blank=True, null=True, verbose_name="Цвет")
    condition = models.CharField(max_length=60, choices=CarStatus.choices(), verbose_name='Статус авто')
    price = models.PositiveIntegerField(verbose_name='Цена, USD')
    producers = models.ForeignKey(Producer, related_name='producers', on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Поставщик')
    auto_shows = models.ForeignKey(AutoShow, related_name='auto_shows', on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Автосалон')
    customers = models.ForeignKey(Customer, related_name='customers', on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Покупатель')

    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр автомобиля'
        verbose_name_plural = 'Экземпляры автомобиля'

    def __str__(self):
        return f'{str(self.name)} {self.condition}'
