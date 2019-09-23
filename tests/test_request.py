from unittest import TestCase
import json
from ortb.request import Segment, Data, Geo, User, Device, Producer, Content, Publisher, App, Site


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

    dataDevice = {
        'ua': 'device_ua',
        'geo': dataGeo,
        'dnt': 8,
        'lmt': 9,
        'ip': 'device_ip',
        'ipv6': 'device_ipv6',
        'devicetype': 10,
        'make': 'device_make',
        'model': 'device_model',
        'os': 'device_os',
        'osv': 'device_osv',
        'hwv': 'device_hwv',
        'h': 11,
        'w': 12,
        'ppi': 13,
        'pxratio': 14.14,
        'js': 15,
        'geofetch': 16,
        'flashver': 'device_flashver',
        'language': 'device_language',
        'carrier': 'device_carrier',
        'mccmnc': 'device_mccmnc',
        'connectiontype': 17,
        'ifa': 'device_ifa',
        'didsha1': 'device_didsha1',
        'didmd5': 'device_didmd5',
        'dpidsha1': 'device_dpidsha1',
        'dpidmd5': 'device_dpidmd5',
        'macsha1': 'device_macsha1',
        'macmd5': 'device_macmd5',
        'ext': 'device_ext',
    }

    dataProducer = {
        'id': 'producer_id',
        'name': 'producer_name',
        'cat': ['producer_cat1', 'producer_cat2'],
        'domain': 'producer_domain',
        'ext': 'producer_ext',
    }

    dataContent = {
        'id': 'content_id',
        'episode': 18,
        'title': 'content_title',
        'series': 'content_series',
        'season': 'content_season',
        'artist': 'content_artist',
        'genre': 'content_genre',
        'album': 'content_album',
        'isrc': 'content_isrc',
        'producer': dataProducer,
        'url': 'content_url',
        'cat': ['content_cat1', 'content_cat2'],
        'prodq': 19,
        'videoquality': 20,
        'context': 21,
        'contentrating': 'content_contentrating',
        'userrating': 'content_userrating',
        'qagmediarating': 22,
        'keywords': 'content_keywords',
        'livestream': 23,
        'sourcerelationship': 24,
        'len': 25,
        'language': 'content_language',
        'embeddable': 26,
        'data': [dataData],
        'ext': 'content_ext',
    }

    dataPublisher = {
        'id': 'publisher_id',
        'name': 'publisher_name',
        'cat': ['publisher_cat1', 'publisher_cat2'],
        'domain': 'publisher_domain',
        'ext': 'publisher_ext',
    }

    dataApp = {
        'id': 'app_id',
        'name': 'app_name',
        'bundle': 'app_bundle',
        'domain': 'app_domain',
        'storeurl': 'app_storeurl',
        'cat': ['app_cat1', 'app_cat2'],
        'sectioncat': ['app_cat3', 'app_cat4'],
        'pagecat': ['app_cat5', 'app_cat6'],
        'ver': 'app_ver',
        'privacypolicy': 27,
        'paid': 28,
        'publisher': dataPublisher,
        'content': dataContent,
        'keywords': 'app_keywords',
        'ext': 'app_ext',
    }

    dataSite = {
        'id': 'site_id',
        'name': 'site_name',
        'domain': 'site_domain',
        'cat': ['site_cat1', 'site_cat2'],
        'sectioncat': ['site_cat3', 'site_cat4'],
        'pagecat': ['site_cat5', 'site_cat6'],
        'page': 'site_page',
        'ref': 'site_ref',
        'search': 'site_search',
        'mobile': 29,
        'privacypolicy': 30,
        'publisher': dataPublisher,
        'content': dataContent,
        'keywords': 'site_keywords',
        'ext': 'site_ext',
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

    def test_Device(self):
        obj = self.getObject(Device, self.dataDevice)
        self.checkBasicFields(obj, self.dataDevice)

    def test_Producer(self):
        obj = self.getObject(Producer, self.dataProducer)
        self.checkBasicFields(obj, self.dataProducer)

        self.assertEqual(obj.cat, self.dataProducer['cat'])

    def test_Content(self):
        obj = self.getObject(Content, self.dataContent)
        self.checkBasicFields(obj, self.dataContent)

        self.assertIsInstance(obj.producer, Producer)
        self.assertIsInstance(obj.data[0], Data)

    def test_Publisher(self):
        obj = self.getObject(Publisher, self.dataPublisher)
        self.checkBasicFields(obj, self.dataPublisher)

        self.assertEqual(obj.cat, self.dataPublisher['cat'])

    def test_App(self):
        obj = self.getObject(App, self.dataApp)
        self.checkBasicFields(obj, self.dataApp)

        self.assertIsInstance(obj.publisher, Publisher)
        self.assertIsInstance(obj.content, Content)

    def test_Site(self):
        obj = self.getObject(Site, self.dataSite)
        self.checkBasicFields(obj, self.dataSite)

        self.assertIsInstance(obj.publisher, Publisher)
        self.assertIsInstance(obj.content, Content)
