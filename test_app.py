import pytest

from app import app

@pytest.fixture
def client():
    yield app.test_client()

def test_serves_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Hello World' in response.data

def test_servers_login_page(client):
    response = client.get('/login')

    assert response.status_code == 200
    assert '<form>' in response.data

def test_can_post_to_login(client):
    response = client.post('/login')

    assert response.status_code == 200

def test_accessing_restricted_page_redirects_to_login(client):
    response = client.get('/user_details')

    assert response.status_code == 302

def test_can_read_user_details_when_logged_in(client):
    response = client.post('/login')
    response = client.get('/user_details')

    assert response.status_code == 200
    assert 'Secret details' in response.data
