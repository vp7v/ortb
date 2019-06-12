
from ortb.core import OrtbObject, OrtbArray

class Title(OrtbObject):
    """Title object"""
    _required = {
        'len': int
    }

    _optional = {
        'ext': str
    }

class Image(OrtbObject):
    """The Image object to be used for all image elements of the Native ad such as Icons, Main Image, etc."""
    _optional = {
        'wmin': int,
        'hmin': int,
        'type': int,
        'w': int,
        'h': int,
        'mimes': OrtbArray(str),
        'ext': str,
    }

class Data(OrtbObject):
    """The Data Object is to be used for all non-core elements of the native unit such as Ratings, Review Count, Stars, Download count, descriptions etc. It is also generic for future of Native elements not contemplated at the time of the writing of this document."""
    _required = {
        'type': int
    }

    _optional = {
        'len': int,
        'ext': str,
    }

class Asset(OrtbObject):
    """Asset object. Asset object may contain only one of title, img, data or video"""
    _required = {
        'id': str
    }

    _optional = {
        'required': int,
        'title': Title,
        'img': Image,
        #'video': Video,
        'data': Data,
        'ext': str,
    }

class NativeMarkupRequest(OrtbObject):
    """Native Markup Request Object"""
    _required = {
        'assets': OrtbArray(Asset)
    }

    _optional = {
        'layout': int,
        'adunit': int,
        'ver': str,
        'plcmtcnt': int,
        'seq': int,
        'ext': str,
    }
