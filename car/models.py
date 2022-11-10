from django.db import models

from auto_show.models import AutoShow
from producer.models import Producer
from customer.models import Customer


class Car(models.Model):
    """Model for Car"""

    brand = models.CharField(max_length=50, verbose_name="Бренд")
    model = models.CharField(max_length=50, verbose_name=" Mодель")
    year = models.CharField(max_length=4, verbose_name="Год выпуска")
    description = models.TextField(blank=True, verbose_name='Описание')


    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    @property
    def full_name(self):
        return "{} {} {}".format(self.brand, self.model, self.year)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class CarInstance(models.Model):
    """Model for CarInstance"""

    name = models.ForeignKey(Car, related_name='car_instances', on_delete=models.CASCADE, verbose_name="Автомобиль")
    color = models.CharField(max_length=200, blank=True, null=True, verbose_name="Цвет")
    CONDITION = [('wish_auto_show', 'желаемый для автосалона'), ('wish_customer', 'желаемый для покупателя'),
                 ('at auto_show', 'в автосалоне'), ('at_producer', 'у поставщика'), ('at_customer', 'у покупателя')]
    condition = models.CharField(max_length=40, choices=CONDITION, verbose_name='Статус авто')
    price = models.PositiveIntegerField(verbose_name='Цена, USD')
    producers = models.ForeignKey(Producer, related_name='producers', on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Поставщик')
    auto_shows = models.ForeignKey(AutoShow, related_name='auto_shows', on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Автосалон')
    customers = models.ForeignKey(Customer, related_name='customers', on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Покупатель')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    ### action_producers = models.ForeignKey(ActionProducer, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Акция поставщика")
    # action_auto_shows = models.ForeignKey(ActionAutoShow, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Акция автосалона")
    # price_discount_auto_shows = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой ПП, сделка автосалон-покупатель, USD')
    # price_discount_producers = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой ПП, сделка поставщик-автосалон, USD')
    # price_action_auto_shows = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена по акции автосалона, USD')
    # price_action_producers = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена по акции поставщика, USD')

    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр автомобиля'
        verbose_name_plural = 'Экземпляры автомобиля'

    def __str__(self):
        return f'{str(self.name)} {self.condition}'
