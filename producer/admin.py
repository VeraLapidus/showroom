from django.contrib import admin

from producer.models import Producer, ActionProducer, DiscountProducer


class ProducerAdmin(admin.ModelAdmin):
    """Admin class for Producer"""

    list_display = ('name', 'country', 'balance', 'owner', 'is_active')
    list_editable = ('is_active',)


class ActionProducerAdmin(admin.ModelAdmin):
    """Admin class for ActionProducer"""

    list_display = ('name', 'amount_action', 'date_start', 'date_finish', 'producers', 'is_active')
    list_editable = ('is_active',)


class DiscountProducerAdmin(admin.ModelAdmin):
    """Admin class for DiscountProducer"""

    list_display = ('name', 'amount_discount', 'quantity_cars_max', 'quantity_cars_min', 'producers', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Producer, ProducerAdmin)
admin.site.register(ActionProducer, ActionProducerAdmin)
admin.site.register(DiscountProducer, DiscountProducerAdmin)
