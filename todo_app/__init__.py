import os

from flask import Flask 
from flask import request

def create_app(test_config == None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/rishu')
    def rishu():
        return 'wakanda forever'

    return app