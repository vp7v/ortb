from unittest import TestCase
import json
from ortb.core import OrtbObject

class TestCaseOrtb(TestCase):

    def getObject(self, cls, data):
        j = json.dumps(data)
        obj = cls.from_json(j)
        return obj

    def checkFields(self, obj, data):
        """ Avoiding mass copypaste for every field checking.
        """
        for key, value in data.items():
            prop = getattr(obj, key)

            if isinstance(prop, OrtbObject):
                # Must be checked manually in the test method
                continue

            if type(prop) == list:
                # List elements always has the same type
                if isinstance(prop[0], OrtbObject):
                    continue

            self.assertEqual(value, prop)


    def assertOrtbFields(self, cls, data):
        obj = self.getObject(cls, data)
        self.checkFields(obj, data)

