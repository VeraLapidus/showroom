from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Producer
from .serializers import ProducerSerializer, ProducerSerializerCreate


class ProducerViewSet(mixins.CreateModelMixin,
                      viewsets.ReadOnlyModelViewSet):
    """ Вывод данных для поставщиков с возможностью создания поставщика"""

    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return ProducerSerializerCreate

        return self.serializer_class




def list_producers(request):
    """Функция вывода списка всех поставщиков"""

    producers = Producer.objects.all()
    context = {'producers': producers}
    return render(request, 'list_producers.html', context)
