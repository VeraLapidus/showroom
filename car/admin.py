from django.contrib import admin
from car.models import Car, CarInstance


class CarAdmin(admin.ModelAdmin):
    """Admin class for model Car"""

    list_display = ('brand', 'model', 'year', 'is_active')
    list_editable = ('is_active',)


class CarInstanceAdmin(admin.ModelAdmin):
    """Admin class for model CarInstance"""

    list_display = ('name', 'color', 'price', 'condition', 'producers', 'auto_shows', 'customers', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Car, CarAdmin)
admin.site.register(CarInstance, CarInstanceAdmin)
