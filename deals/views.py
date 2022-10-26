from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from deals.models import Deal
from deals.serializers import DealSerializer


class DealViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод данных для сделок """

    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (IsAdminUser,)




def start_page(request):
    """Функция вывода стартовой страницы"""

    return render(request, 'start_page.html')
