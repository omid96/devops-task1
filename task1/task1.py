import json
from flask import Flask
from flask_restful import Api
from flask_session import Session

from .config import Config
from .index import index_bp
from .status import status_bp

status_api = Api(status_bp)

from . import resource

def create_app(config_file=None):
    app = Flask(__name__)

    if config_file is not None:
        app.config.from_file(config_file, load=json.load)
    else:
        app.config.from_object(Config)

    Session(app)

    app.register_blueprint(status_bp)
    app.register_blueprint(index_bp)

    return app
