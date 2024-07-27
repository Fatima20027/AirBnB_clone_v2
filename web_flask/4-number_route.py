#!/usr/bin/python3

"""
This script starts a Flask web application
The application listens on all available IP addresses (0.0.0.0) and port 5000.
Routes: - /: returns "Hello HBNB!"
         - /hbnb: returns "HBNB"
         - /c/<text>: displays "C"
         - /python/<text>: displays "Python"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Returns:
        str: The string "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns:
        str: The string "HBNB!".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    display “C ” followed by the value of the text variable.
    """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    display “Python ” followed by the value of the text variable.
    The default value of text is “is cool”
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    /number/<n>: display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
