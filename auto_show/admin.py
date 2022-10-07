from django.contrib import admin

from auto_show.models import AutoShow, ActionAutoShow, DiscountAutoShow

admin.site.register(AutoShow)
admin.site.register(ActionAutoShow)
admin.site.register(DiscountAutoShow)