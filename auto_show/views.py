from django.core.mail import send_mail

from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from auto_show.filters import AutoShowFilter
from auto_show.models import AutoShow
from auto_show.serializers import AutoShowSerializer, AutoShowSerializerCreate


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

    # ordering_fields = ['year_foundation']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return AutoShowSerializerCreate

        return self.serializer_class


