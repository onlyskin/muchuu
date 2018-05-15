import os

import json

import pytest
import records

os.environ['MUCHUU_DATABASE_URL'] = 'sqlite://'
os.environ['SECRET_KEY'] = 'secret_key'

from app import app, get_db
app.testing = True

@pytest.fixture
def db():
    with app.app_context():
        db = get_db()
        db.query("create table steps ( step_text text )")
        db.query("insert into steps values ( 'Example step 0' )")
        yield db
        db.query("drop table steps")

@pytest.fixture
def client():
    yield app.test_client()

class TestGetPages():
     def test_serves_index(self, client):
         response = client.get('/')
     
         assert response.status_code == 200
         assert 'Hello World' in response.data
     
     def test_serves_login_page(self, client):
         response = client.get('/login')
     
         assert response.status_code == 200
         assert '<form action="/login" method="post">' in response.data

class TestLoggingIn():
    def test_successful_login_redirects_to_user_details(self, client):
        payload = dict(
            password='good_password',
        )
        response = client.post('/login', data=payload)
    
        assert response.status_code == 302
        assert response.location.endswith('/user_details')
    
    def test_unsuccessful_login_redirects_to_login(self, client):
        payload = dict(
            password='bad_password',
        )
        response = client.post('/login', data=payload)
    
        assert response.status_code == 302
        assert response.location.endswith('/login')

class TestUserDetailsAuthentication():
    def test_cannot_access_details_page_when_not_logged_in(self, client):
        response = client.get('/user_details')
    
        assert response.status_code == 302
    
    def test_can_access_details_page_when_logged_in(self, client):
        login(client)
    
        response = client.get('/user_details')
    
        assert response.status_code == 200
        assert 'Secret details' in response.data

class TestGetsDatabaseUrlFromEnvironment():
    def test_gets_db(self, db):
        assert db.get_table_names() == ['steps']
        steps = db.query('select step_text from steps')
        assert steps[0].step_text == 'Example step 0'

class TestStepsRoute():
    def test_gets_steps_as_json(self, client, db):
        login(client)

        response = client.get('/steps')

        assert json.loads(response.data) == ['Example step 0']

def login(client):
    payload = dict(
        password='good_password',
    )
    response = client.post('/login', data=payload)
