
from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship

from app.lib.enums import PendingStatus
from app.models.base import Base


class Drift:
    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    requester_id = Column(Integer, ForeignKey('user.id'))
    requester_nickname = Column(String(20))

    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))
    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)
    @pending.setter
    def panding(self,status):
        self._pending = status.value


    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')