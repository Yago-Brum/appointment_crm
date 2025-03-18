from rest_framework import serializers
from crm.models.appointment import Appointment, Client
from crm.models.user import CustomUser  # Importando o modelo CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)

class AppointmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())  # Usando PrimaryKeyRelatedField corretamente

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['id', 'owner', 'created_at']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def validate_client(self, value):
        if not Client.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Client not found")
        return value
