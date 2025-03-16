from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from crm.models.client import Client 
from crm.serializers.client import ClientSerializer  

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
