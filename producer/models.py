from django.db import models

from abstract.abstract_models import BaseData, MainData


class Producer(BaseData, MainData):
    amount_of_clients = models.PositiveIntegerField(blank=True, null=True,
                                                    verbose_name='Количество покупателей-автосалонов')

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class ActionProducer(BaseData):
    """Model for Action (Producer offers to an AutoShow)"""

    name = models.CharField(max_length=50, verbose_name='Название')
    amount_action = models.PositiveIntegerField(verbose_name='Скидка в %')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    date_finish = models.DateTimeField(verbose_name='Дата окончания')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name="Поставщик")

    class Meta:
        # ordering = ['date_start']
        verbose_name = 'Акция поставщика'
        verbose_name_plural = 'Акции поставщика'

    def __str__(self):
        return self.name


class DiscountProducer(BaseData):
    """Regular customer discount (Producer offers to an AutoShow)"""

    name = models.CharField(max_length=50, verbose_name='Имя скидки')
    amount_discount = models.PositiveIntegerField(verbose_name='Размер скидки в %')
    quantity_cars_min = models.PositiveIntegerField(blank=True, null=True,
                                                    verbose_name='Min количество приобретенных авто для скидки')
    quantity_cars_max = models.PositiveIntegerField(blank=True, null=True,
                                                    verbose_name='Max количество приобретенных авто для скидки')
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name="Поставщик")

    class Meta:
        # ordering = ['name']
        verbose_name = 'Скидка постоянного клиента поставщика'
        verbose_name_plural = 'Скидки постоянного клиента поставщика'

    def __str__(self):
        return self.name
