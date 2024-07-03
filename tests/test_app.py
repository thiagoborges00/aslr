from http import HTTPStatus

from fastapi.testclient import TestClient

from zero_fast.app import app

client = TestClient(app)

# def test_zero_division():
#     a = 1/0
#     return a


def test_read_root_deve_retornar_ok():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_read_root_retorna_mensagem_ola_mundao():
    response = client.get('/')
    assert response.json() == {'message': 'olá mundão'}
