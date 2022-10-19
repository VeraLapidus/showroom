from django.shortcuts import render
from rest_framework import generics

from .models import Car, CarInstance
from .serializers import CarSerializer, CarAllSerializer, CarInstanceAllSerializer


class CarList(generics.ListCreateAPIView):
    """ Вывод основных данных по всем австомобилям """

    queryset = Car.objects.all()
    serializer_class = CarAllSerializer

class CarView (generics.RetrieveAPIView):
    """  Вывод детальной информации по одному австомобилю """

    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarInstanceList (generics.ListAPIView):
    """ Вывод основных данных по всем экземплярам австомобилей """

    queryset = CarInstance.objects.all()
    serializer_class = CarInstanceAllSerializer