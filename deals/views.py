from django.shortcuts import render
from rest_framework import viewsets

from deals.models import Deal
from deals.serializers import DealSerializer


class DealViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных для сделок """

    queryset = Deal.objects.all()
    serializer_class = DealSerializer




def start_page(request):
    """Функция вывода стартовой страницы"""

    return render(request, 'start_page.html')
