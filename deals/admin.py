from django.contrib import admin

from deals.models import Deal


class DealAdmin(admin.ModelAdmin):
    """Admin class for model Deal"""

    list_display = (
        'name', 'participants', 'producers', 'auto_shows', 'customers', 'car_instances', 'price', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Deal, DealAdmin)
