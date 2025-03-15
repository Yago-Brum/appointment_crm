from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from crm.models.cliente import Cliente 
from crm.serializers.cliente import ClienteSerializer  

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(dono=self.request.user)
