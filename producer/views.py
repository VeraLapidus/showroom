from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from producer.filters import ProducerFilter
from producer.models import Producer
from producer.serializers import ProducerSerializer, ProducerSerializerCreate


class ProducerViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProducerFilter


def get_serializer_class(self, *args, **kwargs):
    if self.request.method == "POST":
        return ProducerSerializerCreate

    return self.serializer_class
