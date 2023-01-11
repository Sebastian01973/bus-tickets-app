from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_extensions import routers

from ticketsApp.views.businessViewSet import BusinessViewSet
from ticketsApp.views.payrollViewSet import PayrollViewSet
from ticketsApp.views.roadViewSet import RoadViewSet
from ticketsApp.views.roleViewSet import RoleViewSet
from ticketsApp.views.userViewSet import UserViewSet
from ticketsApp.views.boxOfficeViewSet import BoxOfficeViewSet
from ticketsApp.views.vehicleViewSet import VehicleViewSet

router = routers.SimpleRouter()
router.register(r'role', RoleViewSet)
router.register(r'user', UserViewSet)
router.register(r'boxOffice', BoxOfficeViewSet)

router.register(r'business', BusinessViewSet)
router.register(r'road', RoadViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'payroll', PayrollViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='ticketsApp:schema'), name='swagger-ui'),
    path('schema/redocs/', SpectacularRedocView.as_view(url_name='ticketsApp:schema'), name='redoc'),

    path('', include(router.urls)),
]
