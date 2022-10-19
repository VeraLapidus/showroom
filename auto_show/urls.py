from django.urls import path, include
from rest_framework import routers

from .views import list_auto_shows, auto_show_detail, AutoShowViewSet

app_name = "auto_show"

router = routers.SimpleRouter()
router.register(r'auto_show', AutoShowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),      # http://127.0.0.1:8000/auto_show/api/auto_show






    path('list_auto_shows/', list_auto_shows, name="list_auto_shows"),
    path('auto_show_detail/<int:id>/', auto_show_detail, name="auto_show_detail"),
]
