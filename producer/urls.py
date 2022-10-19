from django.urls import path, include
from rest_framework import routers

from .views import list_producers, ProducerViewSet

app_name = "producer"

router = routers.SimpleRouter()
router.register(r'producer', ProducerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),    # http://127.0.0.1:8000/producer/api/producer








    path('list_producers/', list_producers, name="list_producers"),
]
