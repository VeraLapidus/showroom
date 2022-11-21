from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from auto_show import tasks
from auto_show.filters import AutoShowFilter
from auto_show.models import AutoShow
from auto_show.serializers import AutoShowSerializer, AutoShowSerializerCreate


class AutoShowViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = AutoShow.objects.all()
    serializer_class = AutoShowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AutoShowFilter  # http://127.0.0.1:8000/auto_show/?country=DE&year_foundation=1999

    # ordering_fields = ['year_foundation']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return AutoShowSerializerCreate

        return self.serializer_class

def one():
    tasks.check_balance.delay()
