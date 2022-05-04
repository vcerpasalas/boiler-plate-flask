from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt, checkpw
from app.helpers.base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    last_name = Column(String(140))
    
    username = Column(String(80), unique=True)
    password = Column(String(120))
    
    rol_id = Column(Integer, ForeignKey('roles.id'), default=1)
    role = relationship('RoleModel', uselist=False, back_populates='users')
    
    def hashPassword(self):
        password_encode = self.password.encode('utf-8')
        password_hash = hashpw(password_encode, gensalt(rounds=10))
        self.password = password_hash.decode('utf-8')
    
    def checkPassword(self, password):
        return checkpw(
            password.encode('utf-8'), self.password.encode('utf-8')
        )
