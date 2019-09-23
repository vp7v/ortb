
import json


class OrtbEncoder(json.JSONEncoder):
    """ JSON Encoder for OrtbObject.
        Most OrtbObjects have repr_json() as return __dict__,
        but it can be overrided, like in request.Native.
    """
    def default(self, obj):
        if isinstance(obj, OrtbObject):
            return obj.repr_json()

        return json.JSONEncoder.default(self, obj)


def OrtbArray(klass):
    """ Array property for OrtbObject.
        For example, 'cat': OrtbArray(str)
    """
    def parser(array):
        ortb_array = [klass(item) for item in array]
        return ortb_array

    return parser


class OrtbObject:
    """ Base OpenRTB object.
        Can be instantiated from dict with all required fields or from json string.
    """
    _required = {}
    _optional = {}

    @classmethod
    def from_json(klass, str_json):
        data = json.loads(str_json)
        return klass(data)

    def __init__(self, fields={}):
        for field, cls in self._required.items():
            if field in fields and fields[field] is not None:
                value = cls(fields[field])
                setattr(self, field, value)
            else:
                raise ValueError("Missing required field %s in structure %s" % (field, fields))

        for field, cls in self._optional.items():
            if field in fields and fields[field] is not None:
                value = cls(fields[field])
                setattr(self, field, value)

    def to_json(self):
        return json.dumps(self, cls=OrtbEncoder)

    def repr_json(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)
