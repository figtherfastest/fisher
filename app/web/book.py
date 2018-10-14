

from flask import jsonify,request
from app.forms.book import searchForm
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    form = searchForm(request.args)
    if form.validate():
        q=form.q.data.strip()
        page = form.page.data
        isbn_or_kety = is_isbn_or_key(q)
        if isbn_or_kety == 'isbn':
            rersult = YuShuBook.search_by_isbn(q)
        else:
            rersult = YuShuBook.search_by_keyword(q,page)
        return jsonify(rersult)
    else:
        return jsonify(form.errors)
