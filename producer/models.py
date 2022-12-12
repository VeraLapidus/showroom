from django.db import models

from abstract.abstract_models import BaseData, MainData


class Producer(BaseData, MainData):
    amount_of_clients = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    def __str__(self):
        return self.name


class ActionProducer(BaseData):
    """Model for Action (Producer offers to an AutoShow)"""

    name = models.CharField(max_length=50)
    amount_action = models.PositiveIntegerField()
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    description = models.TextField(max_length=500, blank=True)
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE)

    class Meta:
        # ordering = ['date_start']
        verbose_name = "Producer's action"
        verbose_name_plural = "Producer's actions"

    def __str__(self):
        return self.name


class DiscountProducer(BaseData):
    """Regular customer discount (Producer offers to an AutoShow)"""

    name = models.CharField(max_length=50)
    amount_discount = models.PositiveIntegerField()
    quantity_cars_min = models.PositiveIntegerField(blank=True, null=True,
                                                    verbose_name="Min car's quantity for discount")
    quantity_cars_max = models.PositiveIntegerField(blank=True, null=True,
                                                    verbose_name="Max car's quantity for discount")
    description = models.TextField(max_length=500, blank=True)
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE)

    class Meta:
        # ordering = ['name']
        verbose_name = "Producer's customer discount"
        verbose_name_plural = "Producer's customer discounts"

    def __str__(self):
        return self.name
