from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import db

class Gift(db.Model):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
