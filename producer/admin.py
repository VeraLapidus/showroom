from django.contrib import admin

from producer.models import Producer, ActionProducer, DiscountProducer

admin.site.register(Producer)
admin.site.register(ActionProducer)
admin.site.register(DiscountProducer)