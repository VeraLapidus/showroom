from django.shortcuts import render
from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer, CustomerAllSerializer


class CustomerList(generics.ListAPIView):
    """ Вывод основных данных по всем клиентам """

    queryset = Customer.objects.all()
    serializer_class = CustomerAllSerializer


class CustomerView(generics.RetrieveAPIView):
    """ Вывод всех данных по одному клиенту """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
