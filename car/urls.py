from rest_framework import routers

from .views import CarViewSet, CarInstanceViewSet

app_name = 'car'

router = routers.SimpleRouter()
router.register(r'car', CarViewSet)
router.register(r'car_instance', CarInstanceViewSet)

urlpatterns = [
]
