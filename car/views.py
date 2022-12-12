from rest_framework import viewsets, mixins
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from car.filters import CarFilter, CarInstanceFilter
from car.models import Car, CarInstance
from car.serializers import CarSerializer, CarInstanceSerializer, CarInstanceSerializerCreate


class CarViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = CarFilter


class CarInstanceViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = CarInstanceFilter
    search_fields = ['name__brand']
    ordering_fields = ['name', 'id']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CarInstanceSerializerCreate

        return self.serializer_class
