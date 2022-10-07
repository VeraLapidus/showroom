from django.db import models
from django_countries.fields import CountryField


class Producer(models.Model):
    """ Класс поставщиков """

    name = models.CharField(max_length=200, verbose_name="Название поставщика")
    country = CountryField(verbose_name="Страна")
    year_foundation = models.PositiveIntegerField(blank=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс поставщика, USD')
    amount_of_clients = models.PositiveIntegerField(blank=True, verbose_name='Количество покупателей-автосалонов')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class ActionProducer(models.Model):
    """ Акция - поставщик проводит для автосалона """

    name = models.CharField(max_length=50, verbose_name='Имя акции')
    amount_action = models.PositiveIntegerField(verbose_name='Размер скидки по акции в %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции (dd.mm.yyyy 00:00:00)')
    description = models.TextField(max_length=500, blank=True)

    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name="Поставщик")

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['date_start']
        verbose_name = 'Акция поставщика'
        verbose_name_plural = 'Акции поставщика'

    def __str__(self):
        return self.name

class DiscountProducer(models.Model):
    """ Скидка постоянного покупателя (поставщик дает скидку автосалону) """

    name = models.CharField(max_length=50, verbose_name='Имя скидки')
    amount_discount = models.PositiveIntegerField(verbose_name='Размер скидки в %')
    quantity_cars_max = models.PositiveIntegerField(blank=True, null=True, verbose_name='Max количество авто для применения скидки')
    quantity_cars_min = models.PositiveIntegerField(blank=True, null=True, verbose_name='Min количество авто для применения скидки')
    description = models.TextField(max_length=500, blank=True)

    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name="Поставщик")

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['name']
        verbose_name = 'Скидка поставщика'
        verbose_name_plural = 'Скидки поставщика'

    def __str__(self):
        return self.name

