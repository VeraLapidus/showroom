from rest_framework import routers

from car.views import CarViewSet, CarInstanceViewSet

app_name = 'car'

router = routers.SimpleRouter()
router.register(r'car', CarViewSet)
router.register(r'car_instance', CarInstanceViewSet)

urlpatterns = [
]
