from django.contrib import admin

from auto_show.models import AutoShow, ActionAutoShow, DiscountAutoShow


class AutoShowAdmin(admin.ModelAdmin):
    """ModelAdmin class for AutoShow"""

    list_display = ('name', 'country', 'balance', 'wish_car', 'owner', 'is_active')
    list_editable = ('is_active',)


class DiscountAutoShowAdmin(admin.ModelAdmin):
    """Admin class for model DiscountAutoShow"""

    list_display = ('auto_shows', 'name', 'amount_discount', 'min_amount_spent', 'max_amount_spent', 'is_active')
    list_editable = ('is_active',)


class ActionAutoShowAdmin(admin.ModelAdmin):
    """Admin class for model ActionAutoShow"""

    list_display = ('name', 'amount_action', 'date_start', 'date_finish', 'auto_shows', 'is_active')
    list_editable = ('is_active',)


admin.site.register(AutoShow, AutoShowAdmin)
admin.site.register(ActionAutoShow, ActionAutoShowAdmin)
admin.site.register(DiscountAutoShow, DiscountAutoShowAdmin)
