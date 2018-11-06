from flask import Flask
from config import config

def create_app(config_name='DEVELOPMENT'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

app = create_app()

if __name__ == '__main__':
    app.run()
