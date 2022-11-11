from rest_framework import routers

from customer.views import CustomerViewSet

app_name = "customer"

router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
]
