from rest_framework import routers

from .views import  AutoShowViewSet

app_name = "auto_show"

router = routers.SimpleRouter()
router.register(r'auto_show', AutoShowViewSet)

urlpatterns = [
]
