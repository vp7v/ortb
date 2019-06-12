from unittest import TestCase
import json
from ortb.native.response import NativeMarkup, Asset, Title, Image, Data, Video, Link, EventTracker


class TestNativeResponse(TestCase):
    dataEventTracker = {
        'event': 2,
        'method': 3,
        'url': 'et_url',
        'customdata': 'et_customdata',
        'ext': 'et_ext',
    }

    dataLink = {
        'url': 'link_url',
        'clicktrackers': ['link_ct_1', 'link_ct_2'],
        'fallback': 'link_fallback',
        'ext': 'link_ext',
    }

    dataVideo = {
        'vasttag': 'video_vasttag'
    }

    dataData = {
        'type': 4,
        'len': 5,
        'value': 'data_value',
        'ext': 'data_ext',
    }

    dataImage = {
        'type': 6,
        'url': 'image_url',
        'w': 7,
        'h': 8,
        'ext': 'image_ext',
    }

    dataTitle = {
        'text': 'title_text',
        'len': 9,
        'ext': 'title_ext',
    }

    dataAsset = {
        'id': 10,
        'required': 11,
        'title': dataTitle,
        'img': dataImage,
        'video': dataVideo,
        'data': dataData,
        'link': dataLink,
        'ext': 'asset_ext',
    }

    dataNativeMarkup = {
        'ver': 'markup_ver',
        'assets': [dataAsset],
        'assetsurl': 'markup_assetsurl',
        'dcourl': 'markup_dcourl',
        'link': dataLink,
        'imptrackers': ['markup_imp1', 'markup_imp2'],
        'eventtrackers': ['markup_event1', 'markup_event2'],
        'privacy': 'markup_privacy',
        'ext': 'markup_ext',
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

    def test_EventTracker(self):
        obj = self.getObject(EventTracker, self.dataEventTracker)
        self.checkBasicFields(obj, self.dataEventTracker)

    def test_Link(self):
        obj = self.getObject(Link, self.dataLink)
        self.checkBasicFields(obj, self.dataLink)

        self.assertEqual(obj.clicktrackers, self.dataLink['clicktrackers'])

    def test_Video(self):
        obj = self.getObject(Video, self.dataVideo)
        self.checkBasicFields(obj, self.dataVideo)

    def test_Data(self):
        obj = self.getObject(Data, self.dataData)
        self.checkBasicFields(obj, self.dataData)

    def test_Image(self):
        obj = self.getObject(Image, self.dataImage)
        self.checkBasicFields(obj, self.dataImage)

    def test_Title(self):
        obj = self.getObject(Title, self.dataTitle)
        self.checkBasicFields(obj, self.dataTitle)

    def test_Asset(self):
        obj = self.getObject(Asset, self.dataAsset)
        self.checkBasicFields(obj, self.dataAsset)

        self.assertIsInstance(obj.title, Title)
        self.assertIsInstance(obj.img, Image)
        self.assertIsInstance(obj.video, Video)
        self.assertIsInstance(obj.data, Data)
        self.assertIsInstance(obj.link, Link)

    def test_NativeMarkup(self):
        obj = self.getObject(NativeMarkup, self.dataNativeMarkup)
        self.checkBasicFields(obj, self.dataNativeMarkup)

        self.assertIsInstance(obj.assets[0], Asset)
        self.assertIsInstance(obj.link, Link)
