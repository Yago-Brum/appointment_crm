from rest_framework import serializers
from crm.models.appointment import Appointment, Client
from crm.models.user import CustomUser  # Importando o modelo CustomUser
from django.utils.timezone import now

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

    def validate_client(self, value):
        if not Client.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Client not found")
        return value
    
    def validate_date_hour(self, value):
        # Only validate future dates for new appointments
        if not self.instance and value < now():
            raise serializers.ValidationError("Appointment date cannot be in the past")
        return value

    def validate(self, data):
        client = data.get('client')
        date_hour = data.get('date_hour')
        instance = getattr(self, 'instance', None)

        # Check for existing appointments at the same time
        existing_appointment = Appointment.objects.filter(
            client=client,
            date_hour=date_hour
        ).exclude(id=instance.id if instance else None).first()

        if existing_appointment:
            raise serializers.ValidationError({
                "date_hour": f"This client already has an appointment at {date_hour}"
            })

        return data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
