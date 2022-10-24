from django.urls import path, include
from rest_framework import routers

from .views import CarViewSet, CarInstanceViewSet

app_name = 'car'

router = routers.SimpleRouter()
router.register(r'car', CarViewSet)
router.register(r'car_instance', CarInstanceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # http://127.0.0.1:8000/car/api/car
                                         # http://127.0.0.1:8000/car/api/car_instance
]
