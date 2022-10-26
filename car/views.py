from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Car, CarInstance
from .serializers import CarSerializer, CarInstanceSerializer, CarInstanceSerializerCreate


class CarViewSet(mixins.CreateModelMixin,
                 viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по автомобилям """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CarInstanceViewSet(mixins.CreateModelMixin,
                 viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по экземплярам австомобилей """

    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CarInstanceSerializerCreate

        return self.serializer_class

