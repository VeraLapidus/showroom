from rest_framework import viewsets, mixins
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import CarFilter, CarInstanceFilter
from .models import Car, CarInstance
from .serializers import CarSerializer, CarInstanceSerializer, CarInstanceSerializerCreate


class CarViewSet(mixins.CreateModelMixin,
                 viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по автомобилям """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = CarFilter        # http://127.0.0.1:8000/car/api/car/?brand=Audi&model=A3&min_year=2015


class CarInstanceViewSet(mixins.CreateModelMixin,
                 viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по экземплярам австомобилей """

    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = CarInstanceFilter  # http://127.0.0.1:8000/car/api/car_instance/?condition=wish_auto_show&max_price=130
    search_fields = ['name__brand']      # http://127.0.0.1:8000/car/api/car_instance/?search=Mercedes
    ordering_fields = ['name', 'id']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CarInstanceSerializerCreate

        return self.serializer_class

