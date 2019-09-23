from tests.core import TestCaseOrtb
from ortb.response import Bid, SeatBid, BidResponse

class TestRequest(TestCaseOrtb):
    dataBid = {
        'id': 'bid_id',
        'impid': 'bid_impid',
        'price': 101.101,
        'nurl': 'bid_nurl',
        'burl': 'bid_burl',
        'lurl': 'bid_lurl',
        'adm': 'bid_adm',
        'adid': 'bid_adid',
        'adomain': ['bid_adomain1', 'bid_adomain2'],
        'bundle': 'bid_bundle',
        'iurl': 'bid_iurl',
        'cid': 'bid_cid',
        'crid': 'bid_crid',
        'tactic': 'bid_tactic',
        'cat': ['bid_cat1', 'bid_cat2'],
        'attr': [102, 103],
        'api': 104,
        'protocol': 105,
        'qagmediarating': 106,
        'language': 'bid_language',
        'dealid': 'bid_dealid',
        'w': 107,
        'h': 108,
        'wratio': 109,
        'hratio': 110,
        'exp': 111,
        'ext': 'bid_ext',
    }

    dataSeatBid = {
        'bid': [dataBid],
        'seat': 'sb_seat',
        'group': 201,
        'ext': 'sb_ext',
    }

    dataBidResponse = {
        'id': 'br_id',
        'seatbid': [dataSeatBid],
        'bidid': 'br_bidid',
        'cur': 'br_cur',
        'customdata': 'br_customdata',
        'nbr': 301,
        'ext': 'br_ext',
    }
    def test_Bid(self):
        self.assertOrtbFields(Bid, self.dataBid)

    def test_SeatBid(self):
        obj = self.getObject(SeatBid, self.dataSeatBid)
        self.checkFields(obj, self.dataSeatBid)

        self.assertIsInstance(obj.bid[0], Bid)

    def test_BidResponse(self):
        obj = self.getObject(BidResponse, self.dataBidResponse)
        self.checkFields(obj, self.dataBidResponse)

        self.assertIsInstance(obj.seatbid[0], SeatBid)
