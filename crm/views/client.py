from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from crm.models.client import Client
from crm.serializers.client import ClientSerializer

class IsAdminOrOwner(BasePermission):
    """Permite que admin veja todos os clientes e usuários comuns vejam apenas os próprios registros."""

    def has_permission(self, request, view):
        return request.user.is_authenticated  # Apenas usuários logados podem acessar

    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin" or obj.owner == request.user

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        if self.request.user.role == "admin":
            return Client.objects.all()  # Admin vê todos os clientes
        return Client.objects.filter(owner=self.request.user)  # Clientes normais só veem os próprios registros
