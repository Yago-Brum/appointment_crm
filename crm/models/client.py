import uuid
from django.db import models
from crm.models.user import CustomUser  # Atualizado

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name  
