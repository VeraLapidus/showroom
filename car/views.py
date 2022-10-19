from rest_framework import viewsets

from .models import Car, CarInstance
from .serializers import CarSerializer, CarInstanceSerializer


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по автомобилям """

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarInstanceViewSet (viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по экземплярам австомобилей """

    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceSerializer