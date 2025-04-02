from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crm.views.client import ClientViewSet
from crm.views.appointment import AppointmentViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')  # /api/clients/
router.register(r'appointments', AppointmentViewSet, basename='appointment')  # /api/appointments/

urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs do router (API)
]
