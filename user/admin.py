from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", 'username', 'email', 'usertype', 'is_active')
    list_editable = ('is_active', 'email', 'usertype')


admin.site.register(User, UserAdmin)
