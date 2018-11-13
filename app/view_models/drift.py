from app.lib.enums import PendingStatus

class DriftCollection:
    def __init__(self,drifts,current_user_id):
        self.data = []
        self.__parse(drifts, current_user_id)

    def __parse(self,drifts,current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift,current_user_id)
            self.data.append(temp.data)


class DriftViewModel:
    def __init__(self,drift,current_user_id):
        self.data = {}
        self.data = self.__parse(drift,current_user_id)

    @staticmethod
    def request_or_gifter(drift,current_user_id):
        if drift.requester_id == current_user_id:
            pass
        else:
            pass

    def __parse(self,drift,current_user_id):
        you_are=self.request_or_gifter(drift,current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending,you_are)
        r = {
            'you_are':you_are,
            'drift_id': drift.id,
            'book_title': drift.gift.book.title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operate':drift.requester_nickname if you_are != 'requester' else drift.requester_nickname,
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }
        return  r
