import pytest

from app import app
app.testing = True

@pytest.fixture
def client():
    yield app.test_client()

def test_serves_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Hello World' in response.data

def test_serves_login_page(client):
    response = client.get('/login')

    assert response.status_code == 200
    assert '<form>' in response.data

def test_logs_in_with_valid_credentials(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)

    assert response.status_code == 200

def test_doesnt_log_in_with_invalid_credentials(client):
    payload = dict(
        password='bad_password',
    )
    response = client.post('/login', data=payload)

    assert response.status_code == 302

def test_cannot_access_details_when_not_logged_in(client):
    response = client.get('/user_details')

    assert response.status_code == 302

def test_can_access_details_when_logged_in(client):
    login(client)

    response = client.get('/user_details')

    assert response.status_code == 200
    assert 'Secret details' in response.data

def login(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)
