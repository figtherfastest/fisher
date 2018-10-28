import json
from flask import jsonify, request, render_template, flash
from app.forms.book import searchForm
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from app.view_models.book import BookViewModel
from . import web


@web.route('/book/search/')
def search():
    form = searchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_kety = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_kety == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books,default=lambda o:o.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail/')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


