import os
from flask import Flask
from app.config.development import DevelopmentConfig
from app.config.production import ProductionConfig
from app.config.testing import TestingConfig
from app.extensions import db, migrate
from app.controllers.blueprints import register_blueprints
from flasgger import Swagger
from app.config.swagger_config import swagger_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    environment = os.getenv("FLASK_ENV", "development")
    if environment == "production":
        app.config.from_object(ProductionConfig)
    elif environment == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    Swagger(app, template=swagger_template)
    migrate.init_app(app, db)
    register_blueprints(app)
    return app
