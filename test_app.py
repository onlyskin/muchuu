import os

import json

import pytest
import records

os.environ['MUCHUU_DATABASE_URL'] = 'sqlite://'
os.environ['SECRET_KEY'] = 'secret_key'
os.environ['MUCHUU_PASSWORD'] = 'good_password'

from app import app, get_db
app.testing = True

@pytest.fixture
def db():
    with app.app_context():
        db = get_db()
        db.query("create table steps ( step_text text )")
        db.query("insert into steps values ( 'Example step 0' )")
        db.query("insert into steps values ( 'Example step 1' )")
        yield db
        db.query("drop table steps")

@pytest.fixture
def client():
    yield app.test_client()

class TestLoginPage():
    def test_serves_login_page(self, client):
        response = client.get('/login')

        assert response.status_code == 200
        assert '<form action="/login" method="post">' in response.data

class TestLoggingIn():
    def test_successful_login_redirects_to_index(self, client):
        payload = dict(
            password='good_password',
        )
        response = client.post('/login', data=payload)
    
        assert response.status_code == 302
        assert response.location.endswith('/')
    
    def test_unsuccessful_login_redirects_to_login(self, client):
        payload = dict(
            password='bad_password',
        )
        response = client.post('/login', data=payload)
    
        assert response.status_code == 302
        assert response.location.endswith('/login')

class TestIndex():
    def test_cannot_access_index_when_not_logged_in(self, client):
        response = client.get('/')
    
        assert response.status_code == 302
    
    def test_can_access_index_when_logged_in(self, client):
        login(client)
    
        response = client.get('/')
    
        assert response.status_code == 200

class TestGetsDatabaseUrlFromEnvironment():
    def test_gets_db(self, db):
        assert db.get_table_names() == ['steps']
        steps = db.query('select step_text from steps')
        assert steps[0].step_text == 'Example step 0'

class TestStepsRoute():
    def test_must_be_logged_in(self, client, db):
        response = client.get('/steps')
        
        assert response.status_code == 302

    def test_gets_steps_as_json(self, client, db):
        login(client)

        response = client.get('/steps')

        assert json.loads(response.data) == [
            'Example step 0',
            'Example step 1',
        ]

class TestStepRoute():
    def test_must_be_logged_in(self, client, db):
        response = client.post('/step', data=dict(step_text=''))
        
        assert response.status_code == 302

    def test_deletes_step(self, client, db):
        login(client)

        payload = dict(
            step_text='Example step 0'
        )
        response = client.delete('/step', data=payload)

        assert json.loads(response.data) == [
            'Example step 1',
        ]

    def test_adds_step(self, client, db):
        login(client)

        payload = dict(
            step_text='Example step 2'
        )
        response = client.post('/step', data=payload)

        assert json.loads(response.data) == [
            'Example step 0',
            'Example step 1',
            'Example step 2',
        ]

def login(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)
