from collections import namedtuple

from app.view_models.book import BookViewModel

MyGift = namedtuple('MyGift',['id','book','wish_count'])
class MyWishes:
    def __init__(self,gifts_of_mine,wish_count_list):
        self.gift = []

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gift = self.__parse()

    def __parse(self):
        temple_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temple_gifts.append(my_gift)
        return temple_gifts

    def __matching(self,gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['isbn']

        r = {
            'wishes_count':count,
            'book':BookViewModel(gift.book),
            'id':gift.id
        }
        return r
        # my_gift = MyGift(gift.id,BookViewModel(gift.book),count)
        # return my_gift




