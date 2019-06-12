
from ortb.core import OrtbObject, OrtbArray


class Bid(OrtbObject):
    """Bid object"""
    _required = {
        'id': str,
        'impid': str,
        'price': str,
    }

    _optional = {
        'adid': str,
        'nurl': str,
        'adm': str,
        'adomain': str,
        'crid': str,
    }


class SeatBid(OrtbObject):
    """ Seat bid """
    _required = {
        'bid': OrtbArray(Bid),
    }


class BidResponse(OrtbObject):
    """ Bid response """
    _required = {
        'id': str,
        'seatbid': OrtbArray(SeatBid)
    }

    _optional = {
        'bidid': str,
        'cur': str,
    }
