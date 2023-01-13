from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_extensions import routers

from ticketsApp.views.businessViewSet import BusinessViewSet
from ticketsApp.views.changePasswordViewSet import ChangePasswordViewSet
from ticketsApp.views.payrollViewSet import PayrollViewSet
from ticketsApp.views.roadViewSet import RoadViewSet
from ticketsApp.views.roleViewSet import RoleViewSet
from ticketsApp.views.userViewSet import UserViewSet
from ticketsApp.views.vehicleViewSet import VehicleViewSet
from ticketsApp.views.clientViewSet import ClientViewSet
from ticketsApp.views.boxOfficeViewSet import BoxOfficeCreateView
from ticketsApp.views.ticketViewSet import TicketViewSet

from ticketsApp.views.loginViewSet import ExampleView

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = routers.SimpleRouter()
router.register(r'role', RoleViewSet)
router.register(r'user', UserViewSet)

router.register(r'business', BusinessViewSet)
router.register(r'road', RoadViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'boxOffice', BoxOfficeCreateView)
router.register(r'client', ClientViewSet)
router.register(r'ticket', TicketViewSet)
# router.register(r'changePassword', ChangePasswordViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    # path('log/', ExampleView.as_view()),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='ticketsApp:schema'), name='swagger-ui'),
    path('schema/redocs/', SpectacularRedocView.as_view(url_name='ticketsApp:schema'), name='redoc'),

    path('', include(router.urls)),
]
