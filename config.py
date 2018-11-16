import os

class Config():
    """Config defaults"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    DATABASE_URI = os.getenv("DATABASEURI")

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
    DATABASE_URI = os.getenv("TEST_DATABASEURI")

config = {
    "TESTING": Testing,
    "DEVELOPMENT": Development,
    "PRODUCTION": Production
}
