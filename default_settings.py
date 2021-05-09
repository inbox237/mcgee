import os
import json

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_BINDS = {
    #    "mcgee_mayblack": "postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_mayblack"
    #    }

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

    @property
    def SQLALCHEMY_BINDS(self):
        value = os.environ.get("DB_BINDS")
        if not value:
            raise ValueError("DB_BINDS is not set")

        return json.loads(value)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()