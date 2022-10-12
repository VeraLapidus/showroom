from django.urls import path

from producer.views import list_producers

app_name = "producer"

urlpatterns = [
    path('list_producers/', list_producers, name="list_producers"),
]