# from app import create_app
from flask import Flask
from config import config

def create_app(config_name="DEVELOPMENT"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    from app.api.v1 import v1
    api.register
    return app

app = create_app()

@app.route('/')
def home():
    return 'Moin moin'

if __name__ == '__main__':
    app.run()
