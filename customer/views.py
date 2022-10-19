from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(mixins.CreateModelMixin,
                   viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по клиентам """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer









def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
