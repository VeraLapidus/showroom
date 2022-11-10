from django.db import models

from auto_show.models import DiscountAutoShow


class Customer(models.Model):
    """Model for Customer"""

    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    year_of_birth = models.PositiveIntegerField(blank=True, null=True, verbose_name='Год рождения')
    balance = models.IntegerField(default=0, verbose_name='Баланс, USD')
    discount_auto_shows = models.ForeignKey(DiscountAutoShow, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name="Скидка автосалона")

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        # ordering = ['last_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
