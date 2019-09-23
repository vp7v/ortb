from tests.core import TestCaseOrtb
from ortb.native.response import NativeMarkup, Asset, Title, Image, Data, Video, Link, EventTracker


class TestNativeResponse(TestCaseOrtb):
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

    def test_EventTracker(self):
        self.assertOrtbFields(EventTracker, self.dataEventTracker)

    def test_Link(self):
        self.assertOrtbFields(Link, self.dataLink)

    def test_Video(self):
        self.assertOrtbFields(Video, self.dataVideo)

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
        self.assertIsInstance(obj.link, Link)

    def test_NativeMarkup(self):
        obj = self.getObject(NativeMarkup, self.dataNativeMarkup)
        self.checkFields(obj, self.dataNativeMarkup)

        self.assertIsInstance(obj.assets[0], Asset)
        self.assertIsInstance(obj.link, Link)
