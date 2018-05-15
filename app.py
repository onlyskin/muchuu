import os

import records
from flask import Flask, request, redirect, jsonify, g, current_app
from flask_login import LoginManager, login_user, login_required

from user import User
from steps_manager import StepsManager

def get_db():
    if 'db' not in g:
        g.db = records.Database(current_app.config['DATABASE_URL'])
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['DATABASE_URL'] = os.environ['MUCHUU_DATABASE_URL']
login_manager = LoginManager(app)
login_manager.login_view = "login"

my_user = User()

@login_manager.user_loader
def load_user(user_id):
    return my_user

@app.route('/')
def index():
    return 'Hello World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
        <form action="/login" method="post">
        <label for="password-input">Password:</label>
        <input type="password" id="password-input" name="password"></input>
        <input type="submit" value="login"></input>
        </form>
        '''

    if not valid_password(request):
        return redirect("login")

    login_user(my_user)
    return redirect("user_details")

def valid_password(request):
    return request.form['password'] == os.environ['MUCHUU_PASSWORD']

@app.route('/user_details')
@login_required
def user_details():
    return 'Secret details'

@app.route('/steps')
@login_required
def steps():
    steps_manager = StepsManager(get_db())
    steps = steps_manager.get_steps()
    return jsonify(steps)

@app.route('/step', methods=['POST', 'DELETE'])
@login_required
def step():
    steps_manager = StepsManager(get_db())
    step_text = request.form['step_text']

    if request.method == 'DELETE':
        steps_manager.delete_step(step_text)
    else:
        steps_manager.add_step(step_text)

    new_steps = steps_manager.get_steps()
    return jsonify(new_steps)
