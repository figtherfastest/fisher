from flask import current_app

from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'MY_gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans+=current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit(gift)
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
