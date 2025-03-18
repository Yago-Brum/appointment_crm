import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    
    # Registra o usuário e obtém o token
    response = client.post("/auth/register/", {"username": "testuser", "password": "testpass"}, format="json")
    
    assert response.status_code == 201, f"Erro no registro: {response.data}"
    assert "access" in response.data
    assert "refresh" in response.data

    # Armazena o token de acesso para o próximo teste
    access_token = response.data['access']

    # Verifica se o usuário foi criado no banco
    assert User.objects.filter(username="testuser").exists()

    return access_token  # Retorna o token para ser reutilizado

@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    
    # Realiza o registro e obtém o token
    access_token = test_register_user()

    # Agora use o token gerado no registro para autenticar a requisição de login
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    # Tente fazer uma requisição que exige autenticação (por exemplo, acessar nomeações)
    response = client.get("/api/v1/appointments/")  # Substitua pela URL real do seu endpoint

    # Verifique se a resposta tem status 200, indicando que a autenticação foi bem-sucedida
    assert response.status_code == 200, f"Erro ao acessar nomeações: {response.data}"
