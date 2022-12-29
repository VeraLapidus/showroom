from rest_framework import routers

from user.views import UserViewSet

app_name = "user"

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
]
