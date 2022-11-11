from django.db import models
from django.urls import reverse

from additional.models import BaseData, MainData


class AutoShow(BaseData, MainData):
    """Model for AutoShow"""

    wish_cars = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Авто к приобретению")
    list_auto = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список авто салона")
    list_producers = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список поставщиков")
    list_customers = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список покупателей")

    # discount_producers = models.ForeignKey(DiscountProducer, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Скидка поставщика")
    # action_producers = models.ForeignKey(ActionProducer, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Акция поставщика")

    class Meta:
        # ordering = ['name']
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('auto_show:auto_show_detail', args=[self.id])


class ActionAutoShow(BaseData):
    """Model for Action (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50, verbose_name='Имя')
    amount_action = models.PositiveIntegerField(verbose_name='Скидка в %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, verbose_name='Автосалон')

    class Meta:
        # ordering = ['date_start']
        verbose_name = 'Акция автосалона'
        verbose_name_plural = 'Акции автосалона'

    def __str__(self):
        return self.name


class DiscountAutoShow(BaseData):
    """Regular customer discount (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50, verbose_name='Название')
    amount_discount = models.PositiveIntegerField(verbose_name='Размер скидки в %')
    max_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Max сумма покупок для скидки')
    min_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Min сумма покупок для скидки')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, verbose_name='Автосалон')

    class Meta:
        # ordering = ['name']
        verbose_name = 'Скидка постоянного клиента автосалона'
        verbose_name_plural = 'Скидки постоянного клиента автосалона'

    def __str__(self):
        return self.name
