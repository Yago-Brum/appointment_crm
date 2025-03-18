import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from crm.models.client import Client
from crm.models.appointment import Appointment
from datetime import datetime, timezone

User = get_user_model()

@pytest.mark.django_db
def test_create_appointment():
    user = User.objects.create_user(username="owner", password="testpass")
    client = Client.objects.create(name="Carlos", email="carlos@email.com", owner=user)

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.post("/api/v1/appointments/", {
        "client": str(client.id),
        "date_hour": datetime(2025, 12, 20, 10, 0, tzinfo=timezone.utc).isoformat(),
        "description": "Consulta médica"
    }, format="json")

    assert response.status_code == 201
    assert Appointment.objects.count() == 1

@pytest.mark.django_db
def test_list_appointments():
    user = User.objects.create_user(username="owner", password="testpass")
    client = Client.objects.create(name="Ana", email="ana@email.com", owner=user)
    Appointment.objects.create(client=client, date_hour="2025-12-20T10:00:00Z", description="Consulta", owner=user)

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get("/api/v1/appointments/")
    
    assert response.status_code == 200
    assert len(response.data) == 1
