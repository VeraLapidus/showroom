from django.urls import path

from customer.views import list_customers

app_name = "customer"

urlpatterns = [
    path('list_customers/', list_customers, name="list_customers"),
]