from rest_framework import serializers
from crm.models.client import Client 

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'phone', 'created_at', 'owner')
        read_only_fields = ('id', 'created_at', 'owner') #impedir que o owner seja editado diretamente

    def create(self, validated_data):
      validated_data['owner'] = self.context['request'].user
      return super().create(validated_data)