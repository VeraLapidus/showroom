from django.contrib import admin

from producer.models import Producer, ActionProducer, DiscountProducer


class ProducerAdmin(admin.ModelAdmin):
    """Класс для админки модели Producer"""

    list_display = ('name', 'country', 'balance', 'amount_of_clients', 'is_active')
    list_editable = ('is_active',)


class ActionProducerAdmin(admin.ModelAdmin):
    """Класс для админки модели ActionProducer"""

    list_display = ('name', 'amount_action', 'date_start', 'date_finish', 'producers', 'is_active')
    list_editable = ('is_active',)


class DiscountProducerAdmin(admin.ModelAdmin):
    """Класс для админки модели DiscountProducer"""

    list_display = ('name', 'amount_discount', 'quantity_cars_max', 'quantity_cars_min', 'producers', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Producer, ProducerAdmin)
admin.site.register(ActionProducer, ActionProducerAdmin)
admin.site.register(DiscountProducer, DiscountProducerAdmin)