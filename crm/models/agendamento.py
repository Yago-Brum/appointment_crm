import uuid
from django.db import models
from django.contrib.auth.models import User
from crm.models.cliente import Cliente  # Importação corrigida

class Agendamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_hora}"
