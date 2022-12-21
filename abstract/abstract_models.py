from django.db import models
from django_countries.fields import CountryField


class BaseData(models.Model):
    """Abstract model - activation, creating, updating data for all models"""

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MainData(models.Model):
    """Abstract model - initial data for AutoShow, Producer"""

    name = models.CharField(max_length=200)
    country = CountryField()
    year_foundation = models.PositiveIntegerField(blank=True, null=True)
    balance = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    class Meta:
        abstract = True
