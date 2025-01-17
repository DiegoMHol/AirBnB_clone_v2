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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
