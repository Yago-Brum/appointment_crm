from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crm.views import cliente, agendamento

router = DefaultRouter()
router.register(r'clientes', cliente.ClienteViewSet)
router.register(r'agendamentos', agendamento.AgendamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
