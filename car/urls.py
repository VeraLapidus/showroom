from django.urls import path

from .views import CarList, CarView, CarInstanceList

app_name = 'car'

urlpatterns = [
    path('api/cars_list', CarList.as_view()),
    path('api/car/<int:pk>', CarView.as_view()),
    path('api/car_instances_list', CarInstanceList.as_view()),
]
