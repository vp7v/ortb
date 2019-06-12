from ortb.core import OrtbObject, OrtbArray


class EventTracker(OrtbObject):

    _required = {
        'event': int,
        'method': int,
    }

    _optional = {
        'url': str,
        'customdata': str,
        'ext': str,
    }


class Link(OrtbObject):

    _required = {
        'url': str,
    }

    _optional = {
        'clicktrackers': OrtbArray(str),
        'fallback': str,
        'ext': str,
    }


class Video(OrtbObject):

    _required = {
        'vasttag': str,
    }


class Data(OrtbObject):

    _required = {
        'value': str,
    }

    _optional = {
        'type': int,
        'len': int,
        'ext': str,
    }


class Image(OrtbObject):

    _required = {
        'url': str,
    }

    _optional = {
        'type': int,
        'w': int,
        'h': int,
        'ext': str,
    }


class Title(OrtbObject):

    _required = {
        'text': str,
    }

    _optional = {
        'len': int,
        'ext': str,
    }


class Asset(OrtbObject):

    _optional = {
        'id': int,
        'required': int,
        'title': Title,
        'img': Image,
        'video': Video,
        'data': Data,
        'link': Link,
        'ext': str,
    }


class NativeMarkup(OrtbObject):

    _required = {
        'link': Link,
    }

    _optional = {
        'ver': str,
        'assets': OrtbArray(Asset),
        'assetsurl': str,
        'dcourl': str,
        'imptrackers': OrtbArray(str),
        'jstracker': str,
        'eventtrackers': OrtbArray(str),
        'privacy': str,
        'ext': str,
    }
