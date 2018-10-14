# 对一些函数的封装

def is_isbn_or_key(word):
    isbn_or_kety = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_kety = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_kety = 'isbn'
    return isbn_or_kety
