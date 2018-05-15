from flask import Flask, request, redirect
from flask_login import LoginManager, login_user, login_required

from user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
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

@app.route('/user_details')
@login_required
def user_details():
    return 'Secret details'

def valid_password(request):
    return request.form['password'] == 'good_password'
