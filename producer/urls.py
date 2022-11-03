from rest_framework import routers

from .views import ProducerViewSet

app_name = "producer"

router = routers.SimpleRouter()
router.register(r'producer', ProducerViewSet)

urlpatterns = [
]
