from tests.core import TestCaseOrtb
from ortb.native.request import NativeMarkup, Asset, Title, Image, Video, Data, EventTrackers


class TestNativeRequest(TestCaseOrtb):
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

    def test_EventTracker(self):
        self.assertOrtbFields(EventTrackers, self.dataEventTrackers)

    def test_Data(self):
        self.assertOrtbFields(Data, self.dataData)

    def test_Image(self):
        self.assertOrtbFields(Image, self.dataImage)

    def test_Title(self):
        self.assertOrtbFields(Title, self.dataTitle)

    def test_Asset(self):
        obj = self.getObject(Asset, self.dataAsset)
        self.checkFields(obj, self.dataAsset)

        self.assertIsInstance(obj.title, Title)
        self.assertIsInstance(obj.img, Image)
        self.assertIsInstance(obj.video, Video)
        self.assertIsInstance(obj.data, Data)

    def test_NativeMarkup(self):
        obj = self.getObject(NativeMarkup, self.dataNativeMarkup)
        self.checkFields(obj, self.dataNativeMarkup)

        self.assertIsInstance(obj.assets[0], Asset)
        self.assertIsInstance(obj.eventtrackers[0], EventTrackers)
