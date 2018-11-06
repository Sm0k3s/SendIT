import os

class Config():
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class Development(Config):
    """Development config class"""
    DEBUG = True


class Production(Config):
    """Production config class"""
    DEBUG = False
    TESTING = False

class Testing(Config):
    """Testing config class"""
    TESTING = True
    DEBUG = True

config = {
    "TESTING": Testing,
    "DEVELOPMENT": Development,
    "PRODUCTION": Production
}
