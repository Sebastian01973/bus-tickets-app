from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_extensions import routers

from ticketsApp.views.roleViewSet import RoleViewSet
from ticketsApp.views.userViewSet import UserViewSet

router = routers.SimpleRouter()
router.register(r'role', RoleViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='ticketsApp:schema'), name='swagger-ui'),
    path('schema/redocs/', SpectacularRedocView.as_view(url_name='ticketsApp:schema'), name='redoc'),


    path('', include(router.urls)),
]
