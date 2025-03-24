from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from crm.models.appointment import Appointment
from crm.serializers.appointment import AppointmentSerializer

# Classe de paginação personalizada
class AppointmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = AppointmentPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date_hour', 'client']  # Permite filtrar por data e cliente
    ordering_fields = ['date_hour']            # Permite ordenar pelos compromissos por data
    ordering = ['date_hour']                   # Ordem padrão

    def get_queryset(self):
        user = self.request.user
        print(f"Usuário autenticado: {user}, Superusuário: {user.is_superuser}")
        
        if user.is_superuser:
            return Appointment.objects.all()  # Admin vê todos os compromissos
        return Appointment.objects.filter(owner=user)  # Usuário vê apenas seus compromissos

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_staff:
            return Response({'error': 'Você não tem permissão para editar este compromisso.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_staff:
            return Response({'error': 'Você não tem permissão para excluir este compromisso.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
