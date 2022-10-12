from django.shortcuts import render

from customer.models import Customer


def list_customers(request):
    """Функция вывода списка всех покупателей"""

    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'list_customers.html', context)
