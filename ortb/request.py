import json

from ortb.core import OrtbEncoder, OrtbObject, OrtbArray
from ortb.native.request import NativeMarkup

class Segment(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'value': str,
        'ext': str,
    }

class Data(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'segment': OrtbArray(Segment),
        'ext': str,
    }

class Geo(OrtbObject):
    _optional = {
        'lat': float,
        'lon': float,
        'type': int,
        'accuracy': int,
        'lastfix': int,
        'ipservice': int,
        'country': str,
        'region': str,
        'regionfips104': str,
        'metro': str,
        'city': str,
        'zip': str,
        'utcoffset': int,
        'ext': str,
    }

class User(OrtbObject):

    _optional = {
        'id': str,
        'buyeruid': str,
        'yob': int,
        'gender': str,
        'keywords': str,
        'customdata': str,
        'geo': Geo,
        'data': OrtbArray(Data),
        'ext': str,
    }

class Site(OrtbObject):
    """ Site """
    _optional = {
        'id': str,
        'page': str,
        'ref': str,
        'cat': OrtbArray(str),
        'name': str,
        'domain': str,
    }




class Device(OrtbObject):
    """ Device """
    _optional = {
        'dnt': int,
        'ua': str,
        'ip': str,
        'geo': Geo,
        'language': str,
        'os': str,
        'osv': str,
        'devicetype': int,
    }




class Native(OrtbObject):
    _required = {
        'request': NativeMarkup,
    }

    _optional = {
        'ver': str,
        'api': str,
        'battr': str,
        'ext': str,
    }

    def __init__(self, fields):
        if isinstance(fields['request'], str):
            # native.request could be json string or ready object
            fields['request'] = json.loads(fields['request'])

        if 'native' in fields['request']:
            # In old versions of OpenRTB object NativeMarkupRequest
            # could be presented as a single property 'native'
            fields['request'] = fields['request']['native']

        super().__init__(fields)

    def repr_json(self):
        fields = self.__dict__.copy()
        fields['request'] = json.dumps(fields['request'], cls=OrtbEncoder)
        return fields


class Impression(OrtbObject):
    """ Impression """
    _required = {
        'id': str,
    }

    _optional = {
        'native': Native,
        'bidfloor': str,
        'bidfloorcur': str,
        'secure': int,
    }


class BidRequest(OrtbObject):
    """ Bid request """
    _required = {
        'id': str,
        'imp': OrtbArray(Impression),
    }

    _optional = {
        'site': Site,
        'device': Device,
        'user': User,
        'badv': OrtbArray(str),
        'bcat': OrtbArray(str),
        'test': int,
        'at': int,
    }
