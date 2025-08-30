import requests
import pytest
import re

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

@pytest.mark.login
def test_login_ok():
    """✅ Caso correcto: login devuelve 200 + token"""
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{BASE_URL}/login", headers=HEADERS, json=data)

    assert response.status_code == 200, f"Esperado 200, recibido {response.status_code}"
    json_data = response.json()
    assert "token" in json_data, "No se devolvió token en login correcto"


@pytest.mark.login
def test_login_error():
    """❌ Caso error: login devuelve 400 + mensaje de error"""
    data = {
        "email": "peter@klaven"  # Falta password
    }
    response = requests.post(f"{BASE_URL}/login", headers=HEADERS, json=data)

    assert response.status_code == 400, f"Esperado 400, recibido {response.status_code}"
    json_data = response.json()
    assert "error" in json_data, "No se devolvió mensaje de error"


@pytest.mark.users
def test_get_users_page_2():
    """📄 GET users?page=2 → comprobar lista con emails válidos"""
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)

    assert response.status_code == 200, f"Esperado 200, recibido {response.status_code}"
    json_data = response.json()

    users = json_data.get("data", [])
    assert len(users) > 0, "La lista de usuarios está vacía"

    for user in users:
        email = user.get("email", "")
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), f"Email inválido: {email}"

