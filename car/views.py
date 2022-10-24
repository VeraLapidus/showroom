from rest_framework import viewsets

from .models import Car, CarInstance
from .serializers import CarSerializer, CarInstanceSerializer


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по автомобилям """

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarInstanceViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных по экземплярам австомобилей """

    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceSerializer


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     print(serializer.data)
    #     return super().list(self, request, *args, **kwargs)