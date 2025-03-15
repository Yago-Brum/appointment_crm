from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from crm.models.agendamento import Agendamento  
from crm.serializers.agendamento import AgendamentoSerializer 

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(dono=self.request.user)
