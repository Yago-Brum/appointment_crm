import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from crm.models.client import Client

User = get_user_model()

@pytest.mark.django_db
def test_create_client():
    user = User.objects.create_user(username="owner", password="testpass")
    client = APIClient()
    client.force_authenticate(user=user)
    
    response = client.post("/api/v1/clients/", {"name": "João", "email": "joao@email.com", "phone": "12345678"}, format="json")
    
    assert response.status_code == 201
    assert Client.objects.count() == 1

@pytest.mark.django_db
def test_list_clients():
    user = User.objects.create_user(username="owner", password="testpass")
    Client.objects.create(name="Maria", email="maria@email.com", owner=user)
    
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/v1/clients/")
    
    assert response.status_code == 200
    assert len(response.data) == 1
