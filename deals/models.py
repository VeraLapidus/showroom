from django.db import models

from auto_show.models import Auto_show
from car.models import CarInstance
from customer.models import Customer
from producer.models import Producer


class Deal(models.Model):
    """ Сделки """

    name = models.CharField(max_length=200, blank=True, verbose_name="Название сделки")

    PARTICIPANTS = [('producer-showroom', 'поставщик-автосалон'), ('showroom-customer', 'автосалон-покупатель')]
    participants = models.CharField(max_length=40, choices=PARTICIPANTS, verbose_name='Стороны сделки')
    price = models.PositiveIntegerField(verbose_name='Сумма сделки, USD')

    auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
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


class DiscountAutoShow(models.Model):
    """ Скидка постоянного покупателя (автосалон дает скидку покупателю) """

    name = models.CharField(max_length=50, verbose_name='Имя скидки')
    amount_discount = models.PositiveIntegerField(verbose_name='Размер скидки в %')
    max_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Max сумма всех покупок для применения скидки')
    min_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Min сумма всех покупок для применения скидки')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, verbose_name='Автосалон')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['name']
        verbose_name = 'Скидка автосалона'
        verbose_name_plural = 'Скидки автосалона'

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


class ActionAutoShow(models.Model):
    """ Акция - автосалон проводит для покупателя """

    name = models.CharField(max_length=50, verbose_name='Имя акции')
    amount_action = models.PositiveIntegerField(verbose_name='Размер скидки по акции в %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции (dd.mm.yyyy 00:00:00)')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, verbose_name='Автосалон')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['date_start']
        verbose_name = 'Акция автосалона'
        verbose_name_plural = 'Акции автосалона'

    def __str__(self):
        return self.name