import json

from ortb.core import OrtbEncoder, OrtbObject, OrtbArray
from ortb.native.request import NativeMarkupRequest

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

class Geo(OrtbObject):
    _optional = {
        'country': str,
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

class User(OrtbObject):
    """ User """
    _optional = {
        'id': str,
        'buyeruid': str,
        'yob': int,
        'customdata': str,
    }

class Native(OrtbObject):
    _required = {
        'request': NativeMarkupRequest,
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

