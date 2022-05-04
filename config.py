from os import getenv
from datetime import timedelta

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=6)

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass
