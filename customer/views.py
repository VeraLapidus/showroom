from django.shortcuts import render
from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer


class CustomerList(generics.ListAPIView):
    """ Вывод данных всех клиентов """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer





def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
