from django.db import models

from abstract.abstract_models import BaseData
from auto_show.models import DiscountAutoShow


class Customer(BaseData):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    year_of_birth = models.PositiveIntegerField(blank=True, null=True)
    balance = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    wish_car = models.TextField(
        default='{"brand": "None", "model": "None", "year": "None", "color": "None", "price": "None"}',
        null=True,
        blank=True,
    )
    discount_auto_shows = models.ForeignKey(DiscountAutoShow, blank=True, null=True, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        # ordering = ['last_name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
