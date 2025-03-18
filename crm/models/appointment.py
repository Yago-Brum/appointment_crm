import uuid
from django.db import models
from crm.models.client import Client
from crm.models.user import CustomUser  # Atualizado

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_hour = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.client.name} - {self.date_hour}" 
