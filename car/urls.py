from django.urls import path

from .views import CarList

app_name = 'car'

urlpatterns = [
    path('api/car_list', CarList.as_view()),

]
