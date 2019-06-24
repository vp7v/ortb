from unittest import TestCase
import json
from ortb.native.request import NativeMarkup, Asset, Title, Image, Video, Data, EventTrackers


class TestNativeResponse(TestCase):
    dataEventTrackers = {
        'event': 2,
        'methods': [3, 4],
        'ext': 'et_ext',
    }

    dataData = {
        'type': 5,
        'len': 6,
        'ext': 'data_ext',
    }

    dataVideo = {
        'mimes': ['v_mime1', 'v_mime2'],
        'minduration': 7,
        'maxduration': 8,
        'protocols': [9, 10],
        'ext': 'video_ext',
    }

    dataImage = {
        'type': 11,
        'w': 12,
        'wmin': 13,
        'h': 14,
        'hmin': 15,
        'mimes': ['i_mime1', 'i_mime2'],
        'ext': 'image_ext',
    }

    dataTitle = {
        'len': 16,
        'ext': 'title_ext',
    }

    dataAsset = {
        'id': 17,
        'required': 18,
        'title': dataTitle,
        'img': dataImage,
        'video': dataVideo,
        'data': dataData,
        'ext': 'asset_ext',
    }

    dataNativeMarkup = {
        'ver': 'nm_ver',
        'context': 19,
        'contextsubtype': 20,
        'plcmttype': 21,
        'plcmtcnt': 22,
        'seq': 23,
        'assets': [dataAsset],
        'aurlsupport': 24,
        'durlsupport': 25,
        'eventtrackers': [dataEventTrackers],
        'privacy': 26,
        'ext': 'nm_ext',
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
        obj = self.getObject(EventTrackers, self.dataEventTrackers)
        self.checkBasicFields(obj, self.dataEventTrackers)
        self.assertEqual(obj.methods, self.dataEventTrackers['methods'])

    def test_Data(self):
        obj = self.getObject(Data, self.dataData)
        self.checkBasicFields(obj, self.dataData)

    def test_Image(self):
        obj = self.getObject(Image, self.dataImage)
        self.checkBasicFields(obj, self.dataImage)
        self.assertEqual(obj.mimes, self.dataImage['mimes'])

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

    def test_NativeMarkup(self):
        obj = self.getObject(NativeMarkup, self.dataNativeMarkup)
        self.checkBasicFields(obj, self.dataNativeMarkup)

        self.assertIsInstance(obj.assets[0], Asset)
        self.assertIsInstance(obj.eventtrackers[0], EventTrackers)
