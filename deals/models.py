from django.db import models

from abstract.abstract_models import BaseData
from auto_show.models import AutoShow
from car.models import CarInstance
from customer.models import Customer
from deals.enums import Participants
from producer.models import Producer


class Deal(BaseData):

    name = models.CharField(max_length=200, blank=True)
    participants = models.CharField(max_length=50, choices=Participants.choices())
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True)
    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, blank=True, null=True)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    car_instances = models.ForeignKey(CarInstance, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name']
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'

    def __str__(self):
        return self.name
