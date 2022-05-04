from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig


app = Flask(__name__) # Objeto donde esta la instancia de Flask
app.config.from_object(DevelopmentConfig)
CORS(app)

db = SQLAlchemy(app) # Objeto donde esta la instancia de SQLAlchemy
migrate = Migrate(app, db) # Objeto donde esta la instancia de las migraciones

jwt = JWTManager(app)
