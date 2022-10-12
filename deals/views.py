from django.shortcuts import render

def start_page(request):
    """Функция вывода стартовой страницы"""

    return render(request, 'start_page.html')
