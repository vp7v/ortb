
from ortb.core import OrtbObject, OrtbArray


class EventTrackers(OrtbObject):

    _required = {
        'event': int,
        'methods': OrtbArray(int),
    }

    _optional = {
        'ext': str,
    }


class Data(OrtbObject):

    _required = {
        'type': int,
    }

    _optional = {
        'len': int,
        'ext': str,
    }


class Video(OrtbObject):

    _required = {
        'mimes': OrtbArray(str),
        'minduration': int,
        'maxduration': int,
        'protocols': OrtbArray(int),
    }

    _optional = {
        'ext': str,
    }


class Image(OrtbObject):

    _required = {

    }

    _optional = {
        'type': int,
        'w': int,
        'wmin': int,
        'h': int,
        'hmin': int,
        'mimes': OrtbArray(str),
        'ext': str,
    }


class Title(OrtbObject):

    _required = {
        'len': int
    }

    _optional = {
        'ext': str
    }


class Asset(OrtbObject):

    _required = {
        'id': int
    }

    _optional = {
        'required': int,
        'title': Title,
        'img': Image,
        'video': Video,
        'data': Data,
        'ext': str,
    }


class NativeMarkup(OrtbObject):

    _required = {
        'assets': OrtbArray(Asset)
    }

    _optional = {
        'ver': str,
        'context': int,
        'contextsubtype': int,
        'plcmttype': int,
        'plcmtcnt': int,
        'seq': int,
        'aurlsupport': int,
        'durlsupport': int,
        'eventtrackers': OrtbArray(EventTrackers),
        'privacy': int,
        'ext': str,
    }
