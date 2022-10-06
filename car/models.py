from django.db import models

from deals.models import ActionProducer, ActionAutoShow
from producer.models import Producer
from customer.models import Customer



class Car(models.Model):
    """ Класс автомобилей """

    brand = models.CharField(max_length=50, verbose_name="Бренд автомобиля")
    model = models.CharField(max_length=50, verbose_name=" Mодель автомобиля")
    year = models.CharField(max_length=4, verbose_name="Год автомобиля")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    @property
    def full_name(self):
        return "{} {} {}".format(self.brand, self.model, self.year)

    # @property
    # def full_name(self):
    #     return "%s %s %s" % (self.brand, self.model, self.year)



    class Meta:
        ordering = ['brand, model, year']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.name



class CarInstance(models.Model):
    """ Класс экземпляра автомобиля """

    name = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    color = models.CharField(max_length=200, blank=True, null=True, verbose_name="Цвет автомобиля")
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена, USD')

    CONDITION = [('wish_auto_show', 'желаемый для автосалона'), ('wish_customer', 'желаемый для покупателя'),
                 ('in_showroom', 'в автосалоне'), ('at_producer', 'у производителя'), ('at_customer', 'у покупателя')]
    condition = models.CharField(max_length=40, choices=CONDITION, verbose_name='Статус авто')


    # discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Акция")
    price_discount = models.IntegerField(blank=True, null=True, verbose_name='Цена со скидкой, USD')
    price_action = models.IntegerField(blank=True, null=True, verbose_name='Цена по акции, USD')


    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Производитель')
    # auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')

    action_producers = models.ForeignKey(ActionProducer, on_delete=models.CASCADE, verbose_name="Акция продавца")
    action_auto_shows = models.ForeignKey(ActionAutoShow, on_delete=models.CASCADE, verbose_name="Акция автосалона")


    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')


    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр автомобиля'
        verbose_name_plural = 'Экземпляры автомобиля'

    def __str__(self):
        return self.name