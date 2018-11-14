from datetime  import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy,BaseQuery
from sqlalchemy import Column, SmallInteger, Integer


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        super(Query,self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)




class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger,default=1)
    create_time = Column('create_time',Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self,attrs_dic):
        for key,value in attrs_dic.items():
            if hasattr(self,key) and  key !='id':
                setattr(self,key,value)

    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
    def delete(self):
        self.status = 0