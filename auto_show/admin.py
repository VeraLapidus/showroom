from django.contrib import admin

from auto_show.models import AutoShow, ActionAutoShow, DiscountAutoShow


class AutoShowAdmin(admin.ModelAdmin):
    """Класс для админки модели AutoShow"""

    list_display = ('name', 'country', 'balance', 'wish_cars', 'list_auto', 'is_active')
    list_editable = ('is_active',)

class DiscountAutoShowAdmin(admin.ModelAdmin):
    """Класс для админки модели DiscountAutoShow"""

    list_display = ('name', 'amount_discount', 'max_amount_spent', 'min_amount_spent', 'auto_shows', 'is_active')
    list_editable = ('is_active',)


class ActionAutoShowAdmin(admin.ModelAdmin):
    """Класс для админки модели ActionAutoShow"""

    list_display = ('name', 'amount_action', 'date_start', 'date_finish', 'auto_shows', 'is_active')
    list_editable = ('is_active',)


admin.site.register(AutoShow, AutoShowAdmin)
admin.site.register(ActionAutoShow, ActionAutoShowAdmin)
admin.site.register(DiscountAutoShow, DiscountAutoShowAdmin)