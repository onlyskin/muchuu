import pytest

from app import app

def test_serves_index():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert 'Hello World' in response.data
