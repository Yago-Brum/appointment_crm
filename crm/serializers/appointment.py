from rest_framework import serializers
from crm.models.appointment import Appointment, Client
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)

class AppointmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())  # Permite enviar o ID do cliente

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['id', 'owner', 'create_at']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)