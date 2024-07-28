#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
