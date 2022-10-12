from django.shortcuts import render

from producer.models import Producer


def list_producers(request):
    """Функция вывода списка всех поставщиков"""

    producers = Producer.objects.all()
    context = {'producers': producers}
    return render(request, 'list_producers.html', context)
