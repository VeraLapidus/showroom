from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from auto_show.filters import AutoShowFilter
from auto_show.models import AutoShow
from auto_show.serializers import AutoShowSerializer, AutoShowSerializerCreate
from auto_show.statistics import statistics


class AutoShowViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    queryset = AutoShow.objects.all()
    serializer_class = AutoShowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AutoShowFilter

    @action(methods=['get'], detail=True)
    def stat(self, request, pk=None):
        return Response(statistics(pk))

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return AutoShowSerializerCreate

        return self.serializer_class
