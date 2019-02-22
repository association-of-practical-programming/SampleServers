from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/hello')
def hello():
    return 'Hello, Martha!'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye, Martha!'


@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    return str(int(x) + int(y))


@app.route('/sub')
def sub():
    x = request.args.get('x')
    y = request.args.get('y')
    return str(int(x) - int(y))


@app.route('/exp')
def exp():
    x = request.args.get('x')
    y = request.args.get('y')
    return str(int(x) ** int(y))
