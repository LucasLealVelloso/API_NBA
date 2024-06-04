import pytest
from main import app  #

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    response = client.get('/resultados_nba')
    assert response.status_code == 200
    print("\nTeste realizado com exito!")
    