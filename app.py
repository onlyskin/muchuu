from flask import Flask, request, redirect
from flask_login import LoginManager, login_user

from user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '<form></form>'

    login_user(User())
    return ''

@app.route('/user_details')
def user_details():
    return redirect(login)
