from django.db import models

from abstract.abstract_models import BaseData
from auto_show.models import AutoShow
from car.enums import CarStatus
from producer.models import Producer
from customer.models import Customer


class Car(BaseData):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    description = models.TextField(blank=True)

    @property
    def full_name(self):
        return "{} {} {}".format(self.brand, self.model, self.year)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class CarInstance(BaseData):
    name = models.ForeignKey(Car, related_name='car_instances', on_delete=models.CASCADE)
    color = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=60, choices=CarStatus.choices())
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    producers = models.ForeignKey(Producer, related_name='producers', on_delete=models.CASCADE, blank=True, null=True)
    auto_shows = models.ForeignKey(AutoShow, related_name='auto_shows', on_delete=models.CASCADE, blank=True, null=True)
    customers = models.ForeignKey(Customer, related_name='customers', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Car Instance'
        verbose_name_plural = 'Car Instances'

    def __str__(self):
        return f'{str(self.name)} {self.condition}'
