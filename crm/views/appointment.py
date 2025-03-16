from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from crm.models.appointment import Appointment  
from crm.serializers.appointment import AppointmentSerializer 

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
