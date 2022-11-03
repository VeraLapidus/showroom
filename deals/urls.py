from rest_framework import routers

from deals.views import DealViewSet

app_name = "deals"

router = routers.SimpleRouter()
router.register(r'deal', DealViewSet)

urlpatterns = [
]
