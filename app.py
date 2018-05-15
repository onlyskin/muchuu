from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '<form></form>'

    return ''

@app.route('/user_details')
def user_details():
    return redirect(login)
