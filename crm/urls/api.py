from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crm.views.client import ClientViewSet
from crm.views.appointment import AppointmentViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('api/', include(router.urls)),
]