import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from crm.models.client import Client
from crm.models.appointment import Appointment
from datetime import datetime, timezone
from django.utils.timezone import timedelta

User = get_user_model()

@pytest.mark.django_db
def test_create_appointment():
    print("DEBUG: Teste 'test_create_appointment' iniciou.")
    print("DEBUG: Importação do módulo datetime:", datetime)
    print("DEBUG: Data e hora no momento da execução:", datetime.now(timezone.utc))
    user = User.objects.create_user(username="owner", password="testpass")
    client_instance = Client.objects.create(name="Carlos", email="carlos@email.com", owner=user)

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.post("/api/v1/appointments/", {
        "client": str(client_instance.id),
        "date_hour": (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat(),  # Agora + 5 minutos
        "description": "Consulta médica"
    }, format="json")

    assert response.status_code == 201
    assert Appointment.objects.count() == 1

@pytest.mark.django_db
def test_list_appointments():
    user = User.objects.create_user(username="owner", password="testpass")
    client_instance = Client.objects.create(name="Ana", email="ana@email.com", owner=user)
    Appointment.objects.create(client=client_instance, date_hour="2025-12-20T10:00:00Z", description="Consulta", owner=user)

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get("/api/v1/appointments/", format="json")

    assert response.status_code == 200
    # Se a API usa paginação, os dados estarão na chave "results"
    if isinstance(response.data, dict) and "results" in response.data:
        results = response.data["results"]
    else:
        results = response.data
    assert len(results) == 1

@pytest.mark.django_db
def test_appointment_creation_validation():
    """
    Testa se não é permitido criar um compromisso no passado
    e se há bloqueio para agendamento duplicado para o mesmo cliente no mesmo horário.
    """
    user = User.objects.create_user(username="testuser", password="testpass")
    client_instance = Client.objects.create(name="Cliente Teste", email="cliente@test.com", owner=user)

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    # Tentar criar compromisso no passado
    past_date = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    response = api_client.post("/api/v1/appointments/", {
        "client": str(client_instance.id),
        "date_hour": past_date,
        "description": "Compromisso no passado"
    }, format="json")
    assert response.status_code == 400
    assert "A data e hora não podem estar no passado" in str(response.data)

    # Criar compromisso para o futuro
    future_date = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    response = api_client.post("/api/v1/appointments/", {
        "client": str(client_instance.id),
        "date_hour": future_date,
        "description": "Consulta Médica"
    }, format="json")
    assert response.status_code == 201

    # Tentar criar compromisso duplicado para o mesmo cliente e horário
    response_dup = api_client.post("/api/v1/appointments/", {
        "client": str(client_instance.id),
        "date_hour": future_date,
        "description": "Consulta Duplicada"
    }, format="json")
    assert response_dup.status_code == 400
    assert "já tem um compromisso" in str(response_dup.data)

@pytest.mark.django_db
def test_appointment_pagination_and_filtering():
    """
    Testa se a paginação e os filtros estão funcionando conforme esperado.
    """
    user = User.objects.create_user(username="testuser2", password="testpass")
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    client_instance = Client.objects.create(name="Cliente Paginação", email="paginacao@test.com", owner=user)

    # Criar 15 compromissos para testar paginação
    future_date = datetime.now(timezone.utc) + timedelta(days=2)
    for i in range(15):
        Appointment.objects.create(
            client=client_instance,
            date_hour=(future_date + timedelta(hours=i)),
            description=f"Compromisso {i+1}",
            owner=user
        )

    # Fazer requisição com paginação (page_size=10, por exemplo)
    response = api_client.get("/api/v1/appointments/?page_size=10", format="json")
    assert response.status_code == 200
    # Verifica se o número de resultados na primeira página é 10
    results = response.data.get("results",)
    assert len(results) == 10

    # Testar filtro por client (usando o id do client)
    response_filter = api_client.get(f"/api/v1/appointments/?client={client_instance.id}", format="json")
    assert response_filter.status_code == 200
    for appt in response_filter.data.get("results"):
        assert str(appt["client"]) == str(client_instance.id)