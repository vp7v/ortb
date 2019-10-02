
import json

class OrtbError(Exception):
    pass

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
    def arrayparser(array):
        ortb_array = [klass(item) for item in array]
        return ortb_array

    return arrayparser


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
        self.setattrs(fields, self._required, True)
        self.setattrs(fields, self._optional, False)

    def setattrs(self, fields, proto, required):
        for field, cls in proto.items():
            if None == fields.get(field, None):
                if required:
                    raise OrtbError(f"Missing required {self.__class__} -> {field}")
                continue

            try:
                value = cls(fields[field])
                setattr(self, field, value)
            except ValueError:
                raise OrtbError(f"Error in {self.__class__} -> {field} ({cls.__name__})") from None

    def to_json(self):
        return json.dumps(self, cls=OrtbEncoder)

    def repr_json(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)
