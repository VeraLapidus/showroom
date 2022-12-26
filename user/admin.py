from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'is_auto_show', 'is_customer', 'is_producer', 'is_active')
    list_editable = ('is_active',)


admin.site.register(User, UserAdmin)
