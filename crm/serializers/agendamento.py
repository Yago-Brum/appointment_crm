from rest_framework import serializers
from crm.models.agendamento import Agendamento 

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
