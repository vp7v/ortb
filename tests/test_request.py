from unittest import TestCase
import json
from ortb.request import Segment, Data, Geo, User


class TestRequest(TestCase):
    dataSegment = {
        'id': 'segment_id',
        'name': 'segment_name',
        'value': 'segment_value',
        'ext': 'segment_ext',
    }

    dataData = {
        'id': 'data_id',
        'name': 'data_name',
        'segment': [dataSegment],
        'ext': 'data_ext',
    }

    dataGeo = {
        'lat': 1.1,
        'lon': 2.2,
        'type': 3,
        'accuracy': 4,
        'lastfix': 5,
        'ipservice': 6,
        'country': 'geo_country',
        'region': 'geo_region',
        'regionfips104': 'geo_regionfips104',
        'metro': 'geo_metro',
        'city': 'geo_city',
        'zip': 'geo_zip',
        'utcoffset': 7,
        'ext': 'geo_ext',

    }

    dataUser = {
        'id': 'user_id',
        'buyeruid': 'user_buyeruid',
        'yob': 1919,
        'gender': 'O',
        'keywords': 'list,of,keywords',
        'customdata': 'user_customdata',
        'geo': dataGeo,
        'data': [dataData],
        'ext': 'user_ext',
    }

    def getObject(self, cls, data):
        j = json.dumps(data)
        obj = cls.from_json(j)
        return obj

    def checkBasicFields(self, obj, data):
        """ Avoiding mass copypaste for check every basic field.
            All others fields must be checked manually.
        """
        for key, value in data.items():
            if type(value) not in (int, str):
                continue

            self.assertEqual(value, getattr(obj, key))

    def test_Segment(self):
        obj = self.getObject(Segment, self.dataSegment)
        self.checkBasicFields(obj, self.dataSegment)

    def test_Data(self):
        obj = self.getObject(Data, self.dataData)
        self.checkBasicFields(obj, self.dataData)

        self.assertIsInstance(obj.segment[0], Segment)

    def test_Geo(self):
        obj = self.getObject(Geo, self.dataGeo)
        self.checkBasicFields(obj, self.dataGeo)

    def test_User(self):
        obj = self.getObject(User, self.dataUser)
        self.checkBasicFields(obj, self.dataUser)

        self.assertIsInstance(obj.geo, Geo)
        self.assertIsInstance(obj.data[0], Data)
