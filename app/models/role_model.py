from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.helpers.base_model import BaseModel

class RoleModel(BaseModel):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    
    users = relationship('UserModel', uselist=True, back_populates='role')
