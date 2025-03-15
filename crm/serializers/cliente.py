from rest_framework import serializers
from crm.models.cliente import Cliente 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
