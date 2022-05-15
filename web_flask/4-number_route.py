#!/usr/bin/python3
""" script that starts a Flask web application """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ return string HELLO HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world_hbnb():
    """ String HBNB return """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_world_text(text):
    """ return string c + text var """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_world_python(text='is cool'):
    """ return string c + text var """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_world_int(n):
    """ return n + is a number if n in int """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
