from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, desc, func
from sqlalchemy.orm import relationship
from app.models.base import db
from app.spider.yushu_book import YuShuBook


class Wish(db.Model):
    id = Column(Integer, primary_key=True)
    user  = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launche=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from app.models.gift import Gift
        # 跨模型 跨表查询
        count_ist = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                            Gift.isbn.in_(isbn_list),
                                                                            Gift.status == 1).group_by(Gift.isbn).all()
        count_ist = [{'count': w[0], 'isbn': w[1]} for w in count_ist]
        return count_ist

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

