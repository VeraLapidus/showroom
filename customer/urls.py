from django.urls import path, include
from rest_framework import routers

from .views import list_customers, CustomerViewSet

app_name = "customer"


router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),            # http://127.0.0.1:8000/customer/api/customer




    path('list_customers/', list_customers, name="list_customers"),
]