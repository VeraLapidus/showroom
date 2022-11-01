from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from .filters import AutoShowFilter
from .models import AutoShow
from .serializers import AutoShowSerializer, AutoShowSerializerCreate



class AutoShowViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """  Вывод данных по автосалонам с возможностью создания автосалона """

    queryset = AutoShow.objects.all()
    serializer_class = AutoShowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AutoShowFilter                   # http://127.0.0.1:8000/auto_show/api/auto_show/?country=DE&year_foundation=1999
    # ordering_fields = ['year_foundation']




    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return AutoShowSerializerCreate

        return self.serializer_class















def list_auto_shows(request):
    """Функция вывода списка всех автосалонов"""

    auto_shows = AutoShow.objects.all()
    context = {'auto_shows': auto_shows}
    return render(request, 'list_auto_shows.html', context)

def auto_show_detail(request, id):
    auto_show = get_object_or_404(AutoShow, id=id)
    context = {'auto_show': auto_show}
    return render(request, 'auto_show_detail.html', context)
