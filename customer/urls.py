from django.urls import path

from .views import list_customers, CustomerList, CustomerView

app_name = "customer"

urlpatterns = [
    path('api/customers_list/', CustomerList.as_view()),
    path('api/customer/<int:pk>/', CustomerView.as_view()),




    path('list_customers/', list_customers, name="list_customers"),
]