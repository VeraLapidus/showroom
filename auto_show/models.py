from django.db import models
from abstract.abstract_models import BaseData, MainData
from user.models import User


class AutoShow(BaseData, MainData):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    wish_car = models.TextField(
        default='{"brand": "None", "model": "None", "year": "None", "color": "None", "price": "None"}',
        null=True,
        blank=True,
    )

    list_auto = models.CharField(max_length=1500, blank=True, null=True)
    list_producers = models.CharField(max_length=1500, blank=True, null=True)
    list_customers = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        # ordering = ['name']
        verbose_name = 'AutoShow'
        verbose_name_plural = 'AutoShows'

    def __str__(self):
        return self.name


class ActionAutoShow(BaseData):
    """Model for Action (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50)
    amount_action = models.PositiveIntegerField(verbose_name="Action's amount, %")
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    description = models.TextField(max_length=500, blank=True)
    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE, verbose_name='Car showroom')

    class Meta:
        # ordering = ['date_start']
        verbose_name = "AutoShows action"
        verbose_name_plural = "AutoShows actions"

    def __str__(self):
        return self.name


class DiscountAutoShow(BaseData):
    """Regular customer discount (AutoShow offers to a Customer)"""

    name = models.CharField(max_length=50)
    amount_discount = models.PositiveIntegerField(verbose_name="Discount's amount, %")
    max_amount_spent = models.PositiveIntegerField(blank=True, null=True,
                                                   verbose_name="Max purchase's amount for discount")
    min_amount_spent = models.PositiveIntegerField(blank=True, null=True,
                                                   verbose_name="Min purchase's amount for discount")
    description = models.TextField(max_length=500, blank=True)
    auto_shows = models.ForeignKey(AutoShow, on_delete=models.CASCADE)

    class Meta:
        # ordering = ['name']
        verbose_name = "AutoShows customer discount"
        verbose_name_plural = "AutoShows customer discounts"

    def __str__(self):
        return self.name
