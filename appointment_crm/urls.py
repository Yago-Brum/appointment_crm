from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', include('crm.urls.api')),  # Rota para a API (clientes, agendamentos)
    path('API/auth/', include('crm.urls.auth')),  # Rota para autenticação
]

