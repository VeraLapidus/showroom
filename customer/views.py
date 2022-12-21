from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from customer.filters import CustomerFilter
from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomerSerializerCreate


class CustomerViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter


def get_serializer_class(self, *args, **kwargs):
    if self.request.method == "POST":
        return CustomerSerializerCreate

    return self.serializer_class
