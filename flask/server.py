from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='static',)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/bye')
def Goodbye():
    return 'Goodbye, World!'


@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    return str(int(x) + int(y))


@app.route('/html')
def html():
    return app.send_static_file('index.html')
