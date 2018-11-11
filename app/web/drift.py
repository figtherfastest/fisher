from flask import flash, redirect, url_for, render_template

from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user

# from app.models.gift import is_yourself_gift

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404()

    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))


    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    gifter =current_gift.user.summary
    return render_template('drift.html',gifter = gifter,user_beans = current_user.beans)

@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
