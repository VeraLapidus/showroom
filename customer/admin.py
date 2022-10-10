from django.contrib import admin

from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    """Класс для админки модели Customer"""

    list_display = ('full_name', 'year_of_birth', 'balance', 'discount_auto_shows', 'is_active')
    list_editable = ('is_active',)

admin.site.register(Customer, CustomerAdmin)