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
    assert '<form action="/login" method="post">' in response.data

def test_successful_login_redirects_to_user_details(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)

    assert response.status_code == 302
    assert response.location.endswith('/user_details')

def test_unsuccessful_login_redirects_to_login(client):
    payload = dict(
        password='bad_password',
    )
    response = client.post('/login', data=payload)

    assert response.status_code == 302
    assert response.location.endswith('/login')

def test_cannot_access_details_page_when_not_logged_in(client):
    response = client.get('/user_details')

    assert response.status_code == 302

def test_can_access_details_page_when_logged_in(client):
    login(client)

    response = client.get('/user_details')

    assert response.status_code == 200
    assert 'Secret details' in response.data

def login(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)
