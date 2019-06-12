from unittest import TestCase
import json

from ortb.core import OrtbEncoder, OrtbArray, OrtbObject


class TestCore(TestCase):

    def test_OrtbEncoder(self):
        class OrtbDuck(OrtbObject):
            def __init__(self):
                pass

            def repr_json(self):
                return 'Quack'

        duck = OrtbDuck()
        jsoned = json.dumps(duck, cls=OrtbEncoder)
        self.assertEqual('"Quack"', jsoned)

    def test_OrtbArray(self):
        field = OrtbArray(str)
        check = field([1, 2, '3'])
        self.assertEqual(check, ['1', '2', '3'])

        field = OrtbArray(int)
        check = field(['1', 2, '3'])
        self.assertEqual(check, [1, 2, 3])
