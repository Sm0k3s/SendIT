"""Launches the app"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
from app.api.v2.models.database import Database

def create_app(config_name="DEVELOPMENT"):
    """Initializes the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    Database.initialize(app.config['DATABASE_URI'])
    jwt = JWTManager(app)
    Database.create_all()

    from app.api.v1 import v1
    from app.api.v2 import v2
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
