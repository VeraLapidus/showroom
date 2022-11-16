from django.db import models
from django_countries.fields import CountryField


class BaseData(models.Model):
    """Abstract model - activation, creating, updating data for all models"""

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class MainData (models.Model):
    """Abstract model - initial data for AutoShow, Producer"""

    name = models.CharField(max_length=200, verbose_name="Название")
    country = CountryField(verbose_name="Страна")
    year_foundation = models.PositiveIntegerField(blank=True, null=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс, USD')

    class Meta:
        abstract = True