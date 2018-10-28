
class BookViewModel:
    def __init__(self, book):
        self.title = book['title'],
        self.author = '、'.join(book['author']),
        self.publisher = book['publisher'],
        self.image = book['image'],
        # self.image = book.image[0].large,
        self.price = book['price'],
        self.summary = book['summary'],
        self.pages = book['pages'],
        self.isbn = book['isbn']

    def intro(self):
        intro = filter(lambda x: True if x else False,
                [self.author, self.publisher, self.price]
        )

        return '/'.join(intro)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.book = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

    class _BookViewModel:
        @classmethod
        def package_single(cls, data, keyword):
            returned = {
                'books': [],
                'total': 0,
                'keyword': keyword
            }
            if data:
                returned['total'] = 1
                returned['books'] = [cls._cut_book_data(data)]
            return returned

        @classmethod
        def package_collection(cls, data, keyword):
            returned = {
                'books': [],
                'total': 0,
                'keyword': keyword
            }
            if data:
                returned['total'] = data['total']
                returned['books'] = [cls._cut_book_data(datas) for datas in data['books']]
                print(returned)
            return returned

        @classmethod
        def _cut_book_data(cls, data):
            book = {
                'title': data['title'],
                'author': '、'.join(data['author']),
                'publisher': data['publisher'],
                'image': data['images']['large'],
                'price': data['price'],
                'summary': data['summary'] or "",
                'pages': data['pages'] or ""
            }
            return book
