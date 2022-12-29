from django.contrib import admin

from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """Admin class for Customer"""

    list_display = ('full_name', 'year_of_birth', 'balance', 'owner', 'wish_car',  'is_active')
    list_editable = ('is_active',)


admin.site.register(Customer, CustomerAdmin)
