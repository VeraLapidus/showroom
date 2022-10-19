from django.urls import path, include
from rest_framework import routers

from deals.views import start_page, DealViewSet

app_name = "deals"

router = routers.SimpleRouter()
router.register(r'deal', DealViewSet)

urlpatterns = [
    path('api/', include(router.urls)),          # http://127.0.0.1:8000/api/deal



    path('', start_page, name="start_page"),

]
