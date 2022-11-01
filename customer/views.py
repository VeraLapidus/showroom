from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import CustomerFilter
from .models import Customer
from .serializers import CustomerSerializer, CustomerSerializerCreate


class CustomerViewSet(mixins.CreateModelMixin,
                   viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по клиентам с возможностью создания клиента """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter                        #http://127.0.0.1:8000/customer/api/customer/?last_name=Titov&min_balance=100


def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CustomerSerializerCreate

        return self.serializer_class







def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
