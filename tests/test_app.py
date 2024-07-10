from http import HTTPStatus

# def test_zero_division():
#     a = 1/0
#     return a


def test_read_root_deve_retornar_ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_read_root_retorna_mensagem_ola_mundao(client):
    response = client.get('/')
    assert response.json() == {'message': 'olá mundão'}


def test_list_all_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {[
        {
            'username': 'test',
            'password': '123',
            'email': 'as@as.edu'
        }
    ]}


def test_update_user(client):
    response = client.put('/users/1',
                          json={
                              'username': 'frajoça',
                              'email': 'asdc@qwe.com',
                              'id': 1
                          })
    assert response.json() == {
                              'username': 'frajoça',
                              'email': 'asdc@qwe.com',
                              'id': 1
                          }


def test_remove_user(client):
    response = client.delete('/users/1')
    assert response.json() =={"message": "User deleted"}

    