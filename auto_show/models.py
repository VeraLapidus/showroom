from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField



class AutoShow(models.Model):
    """Model for AutoShow"""

    name = models.CharField(max_length=200, verbose_name="Название автосалона")
    country = CountryField(verbose_name="Страна")
    year_foundation = models.PositiveIntegerField(blank=True, null=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс автосалона, USD')

    wish_cars = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Авто к приобретению")
    list_auto = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список авто салона")
    list_producers = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список поставщиков")
    list_customers = models.CharField(max_length=1500, blank=True, null=True, verbose_name="Список покупателей")

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

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


class ActionAutoShow(models.Model):
    """Model for Action (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50, verbose_name='Имя')
    amount_action = models.PositiveIntegerField(verbose_name='Скидка в %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, verbose_name='Автосалон')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['date_start']
        verbose_name = 'Акция автосалона'
        verbose_name_plural = 'Акции автосалона'

    def __str__(self):
        return self.name


class DiscountAutoShow(models.Model):
    """Regular customer discount (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50, verbose_name='Название')
    amount_discount = models.PositiveIntegerField(verbose_name='Размер скидки в %')
    max_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Max сумма покупок для скидки')
    min_amount_spent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Min сумма покупок для скидки')
    description = models.TextField(max_length=500, blank=True)

    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, verbose_name='Автосалон')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # ordering = ['name']
        verbose_name = 'Скидка постоянного клиента автосалона'
        verbose_name_plural = 'Скидки постоянного клиента автосалона'

    def __str__(self):
        return self.name
