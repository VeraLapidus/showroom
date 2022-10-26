from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Customer
from .serializers import CustomerSerializer, CustomerSerializerCreate


class CustomerViewSet(mixins.CreateModelMixin,
                   viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по клиентам с возможностью создания клиента """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CustomerSerializerCreate

        return self.serializer_class







def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
