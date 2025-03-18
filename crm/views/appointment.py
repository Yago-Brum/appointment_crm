from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from crm.models.appointment import Appointment
from crm.serializers.appointment import AppointmentSerializer

class IsAdminOrOwner(BasePermission):
    """Permite que admin veja todos os agendamentos e usuários comuns vejam apenas os próprios registros."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin" or obj.owner == request.user

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        if self.request.user.role == "admin":
            return Appointment.objects.all()  # Admin vê todos os agendamentos
        return Appointment.objects.filter(owner=self.request.user)  # Cliente só vê os próprios agendamentos
