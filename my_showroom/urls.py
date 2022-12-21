"""my_showroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from auto_show.views import AutoShowViewSet
from car.views import CarViewSet, CarInstanceViewSet
from customer.views import CustomerViewSet
from deals.views import DealViewSet
from my_showroom import settings
from producer.views import ProducerViewSet

router = routers.DefaultRouter()
router.register(r'deal', DealViewSet)
router.register(r'car', CarViewSet)
router.register(r'car_instance', CarInstanceViewSet)
router.register(r'auto_show', AutoShowViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'producer', ProducerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # Simple JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #djoser
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),

    # Session-based authentication   # http://127.0.0.1:8000/api/drf_auth/login/
    path('api/drf_auth/', include('rest_framework.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    # swagger
    schema_view = get_schema_view(
        openapi.Info(
            title="Showroom DRF",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
                  ] + urlpatterns
