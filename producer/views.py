from django.shortcuts import render
from rest_framework import generics

from .models import Producer
from .serializers import ProducerSerializer, ProducerAllSerializer


class ProducerList(generics.ListAPIView):
    """ Вывод основных данных для всех поставщиков """

    queryset = Producer.objects.all()
    serializer_class = ProducerAllSerializer


class ProducerView(generics.RetrieveAPIView):
    """ Вывод всех данных для одного поставщика """

    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer






def list_producers(request):
    """Функция вывода списка всех поставщиков"""

    producers = Producer.objects.all()
    context = {'producers': producers}
    return render(request, 'list_producers.html', context)
