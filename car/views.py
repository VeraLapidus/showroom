from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializers import CarSerializer


class CarList(generics.RetrieveUpdateAPIView):
    """  Вывод данных всех австомобилей """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
