from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from .models import AutoShow
from .serializers import AutoShowSerializer, AutoShowAllSerializer


class AutoShowList(generics.ListAPIView):
    """  Вывод основных данных по всем автосалонам """

    queryset = AutoShow.objects.all()
    serializer_class = AutoShowAllSerializer



class AutoShowView(generics.RetrieveAPIView):
    """  Вывод всех данных по одному автосалону """

    queryset = AutoShow.objects.all()
    serializer_class = AutoShowSerializer



# class AutoShowCreate(generics.CreateAPIView):
#     """  Создание автосалона """
#
#     queryset = AutoShow.objects.all()
#     serializer_class = AutoShowSerializer












def list_auto_shows(request):
    """Функция вывода списка всех автосалонов"""

    auto_shows = AutoShow.objects.all()
    context = {'auto_shows': auto_shows}
    return render(request, 'list_auto_shows.html', context)

def auto_show_detail(request, id):
    auto_show = get_object_or_404(AutoShow, id=id)
    context = {'auto_show': auto_show}
    return render(request, 'auto_show_detail.html', context)
