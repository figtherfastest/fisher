from app.view_models.book import BookViewModel


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse(goods)

    def _parse(self, goods):
        self.total = len(goods)
        self.trades = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
    
class MyTrades:
    def __init__(self,trades_of_mine,trade_count_list):
        self.gift = []

        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list

        self.gift = self.__parse()

    def __parse(self):
        temple_trades = []
        for gift in self.__trades_of_mine:
            my_trade = self.__matching(gift)
            temple_trades.append(my_trade)
        return temple_trades

    def __matching(self,trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['isbn']

        r = {
            'wishes_count':count,
            'book':BookViewModel(trade.book),
            'id':trade.id
        }
        return r
