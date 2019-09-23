
from ortb.core import OrtbObject, OrtbArray


class Bid(OrtbObject):
    _required = {
        'id': str,
        'impid': str,
        'price': float,
    }

    _optional = {
        'nurl': str,
        'burl': str,
        'lurl': str,
        'adm': str,
        'adid': str,
        'adomain': OrtbArray(str),
        'bundle': str,
        'iurl': str,
        'cid': str,
        'crid': str,
        'tactic': str,
        'cat': OrtbArray(str),
        'attr': OrtbArray(int),
        'api': int,
        'protocol': int,
        'qagmediarating': int,
        'language': str,
        'dealid': str,
        'w': int,
        'h': int,
        'wratio': int,
        'hratio': int,
        'exp': int,
        'ext': str,
    }


class SeatBid(OrtbObject):
    _required = {
        'bid': OrtbArray(Bid),
    }

    _optional = {
        'seat': str,
        'group': int,
        'ext': str,
    }

class BidResponse(OrtbObject):
    _required = {
        'id': str,
        'seatbid': OrtbArray(SeatBid)
    }

    _optional = {
        'bidid': str,
        'cur': str,
        'customdata': str,
        'nbr': int,
        'ext': str,
    }
