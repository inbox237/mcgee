import os
import json

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #Backup in case bind not working through .env file:
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

        # Using a normal bind with a .env file resulted in a string error so I was able to get around this by returning a json
        return json.loads(value)

class DevelopmentConfig(Config):
    DEBUG = False
    use_reloader=False

class ProductionConfig(Config):
    DEBUG = False
    use_reloader=False

class TestingConfig(Config):
    TESTING = True
    DEBUG = False

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()