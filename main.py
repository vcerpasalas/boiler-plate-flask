from app import app, db

from app import routers
from app import models

from app.helpers.base_model import BaseModel

BaseModel.set_session(db.session)
