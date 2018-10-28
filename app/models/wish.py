from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationships
from app.models.base import db

class Wish(db.Model):
    id = Column(Integer, primary_key=True)
    user  = relationships('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
