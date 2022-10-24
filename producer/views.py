from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import Producer
from .serializers import ProducerSerializer


class ProducerViewSet(mixins.CreateModelMixin,
                      viewsets.ReadOnlyModelViewSet):
    """ Вывод данных для поставщиков с возможностью создания поставщика"""

    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer






def list_producers(request):
    """Функция вывода списка всех поставщиков"""

    producers = Producer.objects.all()
    context = {'producers': producers}
    return render(request, 'list_producers.html', context)
