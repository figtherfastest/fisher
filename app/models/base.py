from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,SmallInteger
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger,default=1)

    def set_attrs(self,attrs_dic):
        for key,value in attrs_dic.items():
            if hasattr(self,key) and  key !='id':
                setattr(self,key,value)