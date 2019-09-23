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

class Device(OrtbObject):
    _optional = {
        'ua': str,
        'geo': Geo,
        'dnt': int,
        'lmt': int,
        'ip': str,
        'ipv6': str,
        'devicetype': int,
        'make': str,
        'model': str,
        'os': str,
        'osv': str,
        'hwv': str,
        'h': int,
        'w': int,
        'ppi': int,
        'pxratio': float,
        'js': int,
        'geofetch': int,
        'flashver': str,
        'language': str,
        'carrier': str,
        'mccmnc': str,
        'connectiontype': int,
        'ifa': str,
        'didsha1': str,
        'didmd5': str,
        'dpidsha1': str,
        'dpidmd5': str,
        'macsha1': str,
        'macmd5': str,
        'ext': str,
    }

class Producer(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'cat': OrtbArray(str),
        'domain': str,
        'ext': str,
    }

class Content(OrtbObject):
    _optional = {
        'id': str,
        'episode': int,
        'title': str,
        'series': str,
        'season': str,
        'artist': str,
        'genre': str,
        'album': str,
        'isrc': str,
        'producer': Producer,
        'url': str,
        'cat': OrtbArray(str),
        'prodq': int,
        'videoquality': int,
        'context': int,
        'contentrating': str,
        'userrating': str,
        'qagmediarating': int,
        'keywords': str,
        'livestream': int,
        'sourcerelationship': int,
        'len': int,
        'language': str,
        'embeddable': int,
        'data': OrtbArray(Data),
        'ext': str,
    }

class Publisher(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'cat': OrtbArray(str),
        'domain': str,
        'ext': str,
    }

class App(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'bundle': str,
        'domain': str,
        'storeurl': str,
        'cat': OrtbArray(str),
        'sectioncat': OrtbArray(str),
        'pagecat': OrtbArray(str),
        'ver': str,
        'privacypolicy': int,
        'paid': int,
        'publisher': Publisher,
        'content': Content,
        'keywords': str,
        'ext': str,
    }

class Site(OrtbObject):
    _optional = {
        'id': str,
        'name': str,
        'domain': str,
        'cat': OrtbArray(str),
        'sectioncat': OrtbArray(str),
        'pagecat': OrtbArray(str),
        'page': str,
        'ref': str,
        'search': str,
        'mobile': int,
        'privacypolicy': int,
        'publisher': Publisher,
        'content': Content,
        'keywords': str,
        'ext': str,
    }

class Deal(OrtbObject):
    _optional = {
        'id': str,
        'bidfloor': float,
        'bidfloorcur': str,
        'at': int,
        'wseat': OrtbArray(str),
        'wadomain': OrtbArray(str),
        'ext': str,
    }

class Pmp(OrtbObject):
    _optional = {
        'private_auction': int,
        'deals': OrtbArray(Deal),
        'ext': str,
    }

class Format(OrtbObject):
    _optional = {
        'w': int,
        'h': int,
        'wratio': int,
        'hratio': int,
        'wmin': int,
        'ext': str,
    }

class Native(OrtbObject):
    _required = {
        'request': NativeMarkup,
    }

    _optional = {
        'ver': str,
        'api': OrtbArray(int),
        'battr': OrtbArray(int),
        'ext': str,
    }

    def __init__(self, fields):
        if isinstance(fields['request'], str):
            # native.request could be json string or ready object
            fields['request'] = json.loads(fields['request'])

        super().__init__(fields)

    def repr_json(self):
        fields = self.__dict__.copy()
        fields['request'] = json.dumps(fields['request'], cls=OrtbEncoder)
        return fields

class Banner(OrtbObject):
    _optional = {
        'format': OrtbArray(Format),
        'w': int,
        'h': int,
        'wmax': int,
        'wmin': int,
        'hmax': int,
        'hmin': int,
        'btype': OrtbArray(int),
        'battr': OrtbArray(int),
        'pos': int,
        'mimes': OrtbArray(str),
        'topframe': int,
        'expdir': OrtbArray(int),
        'api': OrtbArray(str),
        'id': str,
        'vcm': int,
        'ext': str,
    }

class Audio(OrtbObject):
    _required = {
        'mimes': OrtbArray(str),
    }

    _optional = {
        'minduration': int,
        'maxduration': int,
        'protocols': OrtbArray(int),
        'startdelay': int,
        'sequence': int,
        'battr': OrtbArray(int),
        'maxextended': int,
        'minbitrate': int,
        'bitrate': int,
        'delivery': OrtbArray(int),
        'companionad': OrtbArray(Banner),
        'api': OrtbArray(int),
        'companiontype': OrtbArray(int),
        'maxseq': int,
        'feed': int,
        'stitched': int,
        'nvol': int,
        'ext': str,
    }

class Video(OrtbObject):
    _required = {
        'mimes': OrtbArray(str),
    }

    _optional = {
        'minduration': int,
        'maxduration': int,
        'protocols': OrtbArray(int),
        'protocol': int,
        'w': int,
        'h': int,
        'startdelay': int,
        'placement': int,
        'linearity': int,
        'skip': int,
        'skipmin': int,
        'skipafter': int,
        'sequence': int,
        'battr': OrtbArray(int),
        'maxextended': int,
        'minbitrate': int,
        'maxbitrate': int,
        'boxingallowed': int,
        'playbackmethod': OrtbArray(int),
        'playbackend': int,
        'delivery': OrtbArray(int),
        'pos': int,
        'companionad': OrtbArray(Banner),
        'api': OrtbArray(int),
        'companiontype': OrtbArray(int),
        'ext': str,
    }

class Metric(OrtbObject):
    _required = {
        'type': str,
        'value': float,
    }

    _optional = {
        'vendor': str,
        'ext': str,
    }

class Imp(OrtbObject):
    _required = {
        'id': str,
    }

    _optional = {
        'metric': OrtbArray(Metric),
        'banner': Banner,
        'video': Video,
        'audio': Audio,
        'native': Native,
        'pmp': Pmp,
        'displaymanager': str,
        'displaymanagerver': str,
        'instl': int,
        'tagid': str,
        'bidfloor': float,
        'bidfloorcur': str,
        'clickbrowser': int,
        'secure': int,
        'iframebuster': OrtbArray(str),
        'exp': int,
        'ext': str,
    }

class Regs(OrtbObject):
    _optional = {
        'coppa': int,
        'ext': str,
    }

class Source(OrtbObject):
    _optional = {
        'fd': int,
        'tid': str,
        'pchain': str,
        'ext': str,
    }

class BidRequest(OrtbObject):
    _required = {
        'id': str,
        'imp': OrtbArray(Imp),
    }

    _optional = {
        'site': Site,
        'app': App,
        'device': Device,
        'user': User,
        'test': int,
        'at': int,
        'tmax': int,
        'wseat': OrtbArray(str),
        'bseat': OrtbArray(str),
        'allimps': int,
        'cur': OrtbArray(str),
        'wlang': OrtbArray(str),
        'bcat': OrtbArray(str),
        'badv': OrtbArray(str),
        'bapp': OrtbArray(str),
        'source': Source,
        'regs': Regs,
        'ext': str,
    }
