from tests.core import TestCaseOrtb
import json
from ortb.request import Segment, Data, Geo, User, Device, Producer, Content, \
    Publisher, App, Site, Deal, Pmp, Format, Native, Banner, Audio, Video, \
    Metric, Imp, Regs, Source, BidRequest
from ortb.native.request import NativeMarkup

class TestRequest(TestCaseOrtb):
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

    dataDeal = {
        'id': 'deal_id',
        'bidfloor': 31.31,
        'bidfloorcur': 'deal_bidfloorcur',
        'at': 32,
        'wseat': ['deal_wseat1', 'deal_wseat2'],
        'wadomain': ['deal_wadomain1', 'deal_wadomain2'],
        'ext': 'deal_ext',

    }

    dataPmp = {
        'private_auction': 33,
        'deals': [dataDeal],
        'ext': 'pmp_ext',
    }

    dataFormat = {
        'w': 34,
        'h': 35,
        'wratio': 36,
        'hratio': 37,
        'wmin': 38,
        'ext': 'format_ext',
    }

    dataNative = {
        'request': {'assets': [{'id': 200}]},
        'ver': 'native_ver',
        'api': [201, 202],
        'battr': [203, 204],
        'ext': 'native_ext',
    }

    dataBanner = {
        'format': [dataFormat],
        'w': 60,
        'h': 61,
        'wmax': 62,
        'hmax': 63,
        'wmin': 64,
        'hmin': 65,
        'btype': [66, 67],
        'battr': [68, 69],
        'pos': 70,
        'mimes': ['banner_mime1', 'banner_mime2'],
        'topframe': 71,
        'expdir': [72, 73],
        'api': [74, 75],
        'id': 'banner_id',
        'vcm': 76,
        'ext': 'banner_ext',
    }

    dataAudio = {
        'mimes': ['audio_mime1', 'audio_mime2'],
        'minduration': 39,
        'maxduration': 40,
        'protocols': [41, 42],
        'startdelay': 43,
        'sequence': 44,
        'battr': [45, 46],
        'maxextended': 47,
        'minbitrate': 48,
        'bitrate': 49,
        'delivery': [50, 51],
        'companionad': [dataBanner],
        'api': [52, 53],
        'companiontype': [54, 55],
        'maxseq': 56,
        'feed': 57,
        'stitched': 58,
        'nvol': 59,
        'ext': 'audio_ext',
    }

    dataVideo = {
        'mimes': ['video_mime1', 'video_mime2'],
        'minduration': 100,
        'maxduration': 101,
        'protocols': [102, 103],
        'protocol': 104,
        'w': 105,
        'h': 106,
        'startdelay': 107,
        'placement': 108,
        'linearity': 109,
        'skip': 110,
        'skipmin': 111,
        'skipafter': 112,
        'sequence': 113,
        'battr': [114, 115],
        'maxextended': 116,
        'minbitrate': 117,
        'maxbitrate': 118,
        'boxingallowed': 119,
        'playbackmethod': [120, 121],
        'playbackend': 122,
        'delivery': [123, 124],
        'pos': 125,
        'companionad': [dataBanner],
        'api': [126, 127],
        'companiontype': [128, 129],
        'ext': 'video_ext',

    }

    dataMetric = {
        'type': 'metric_type',
        'value': 301.301,
        'vendor': 'metric_vendor',
        'ext': 'metric_ext',
    }

    dataImp = {
        'id': 'imp_id',
        'metric': [dataMetric],
        'banner': dataBanner,
        'video': dataVideo,
        'audio': dataAudio,
        'native': dataNative,
        'pmp': dataPmp,
        'displaymanager': 'imp_displaymanager',
        'displaymanagerver': 'imp_displaymanagerver',
        'instl': 401,
        'tagid': 'imp_tagid',
        'bidfloor': 402.402,
        'bidfloorcur': 'imp_bidfloorcur',
        'clickbrowser': 403,
        'secure': 404,
        'iframebuster': ['imp_iframebuster1', 'imp_iframebuster2'],
        'exp': 405,
        'ext': 'imp_ext',
    }

    dataRegs = {
        'coppa': 501,
        'ext': 'regs_ext',
    }

    dataSource = {
        'fd': 601,
        'tid': 'source_tid',
        'pchain': 'source_pchain',
        'ext': 'source_ext',
    }

    dataBidRequest = {
        'id': 'br_id',
        'imp': [dataImp],
        'site': dataSite,
        'app': dataApp,
        'device': dataDevice,
        'user': dataUser,
        'test': 601,
        'at': 602,
        'tmax': 603,
        'wseat': ['br_wseat1', 'br_wseat2'],
        'bseat': ['br_bseat1', 'br_bseat2'],
        'allimps': 604,
        'cur': ['br_cur1', 'br_cur2'],
        'wlang': ['br_wlang1', 'br_wlang2'],
        'bcat': ['br_bcat1', 'br_bcat2'],
        'badv': ['br_badv1', 'br_badv2'],
        'bapp': ['br_bapp1', 'br_bapp2'],
        'source': dataSource,
        'regs': dataRegs,
        'ext': 'br_ext',
    }

    def test_Segment(self):
        self.assertOrtbFields(Segment, self.dataSegment)

    def test_Data(self):
        obj = self.getObject(Data, self.dataData)
        self.checkFields(obj, self.dataData)

        self.assertIsInstance(obj.segment[0], Segment)

    def test_Geo(self):
        self.assertOrtbFields(Geo, self.dataGeo)

    def test_User(self):
        obj = self.getObject(User, self.dataUser)
        self.checkFields(obj, self.dataUser)

        self.assertIsInstance(obj.geo, Geo)
        self.assertIsInstance(obj.data[0], Data)

    def test_Device(self):
        self.assertOrtbFields(Device, self.dataDevice)

    def test_Producer(self):
        self.assertOrtbFields(Producer, self.dataProducer)

    def test_Content(self):
        obj = self.getObject(Content, self.dataContent)
        self.checkFields(obj, self.dataContent)

        self.assertIsInstance(obj.producer, Producer)
        self.assertIsInstance(obj.data[0], Data)

    def test_Publisher(self):
        self.assertOrtbFields(Publisher, self.dataPublisher)

    def test_App(self):
        obj = self.getObject(App, self.dataApp)
        self.checkFields(obj, self.dataApp)

        self.assertIsInstance(obj.publisher, Publisher)
        self.assertIsInstance(obj.content, Content)

    def test_Site(self):
        obj = self.getObject(Site, self.dataSite)
        self.checkFields(obj, self.dataSite)

        self.assertIsInstance(obj.publisher, Publisher)
        self.assertIsInstance(obj.content, Content)

    def test_Deal(self):
        self.assertOrtbFields(Deal, self.dataDeal)

    def test_Pmp(self):
        obj = self.getObject(Pmp, self.dataPmp)
        self.checkFields(obj, self.dataPmp)

        self.assertIsInstance(obj.deals[0], Deal)

    def test_Format(self):
        self.assertOrtbFields(Format, self.dataFormat)

    def test_Native(self):
        obj = self.getObject(Native, self.dataNative)
        self.checkFields(obj, self.dataNative)

        self.assertIsInstance(obj.request, NativeMarkup)

        self.dataNative['request'] = json.dumps(self.dataNative['request'])
        obj = self.getObject(Native, self.dataNative)
        self.assertIsInstance(obj.request, NativeMarkup)

    def test_Banner(self):
        obj = self.getObject(Banner, self.dataBanner)
        self.checkFields(obj, self.dataBanner)

        self.assertIsInstance(obj.format[0], Format)

    def test_Audio(self):
        obj = self.getObject(Audio, self.dataAudio)
        self.checkFields(obj, self.dataAudio)

        self.assertIsInstance(obj.companionad[0], Banner)

    def test_Video(self):
        obj = self.getObject(Video, self.dataVideo)
        self.checkFields(obj, self.dataVideo)

        self.assertIsInstance(obj.companionad[0], Banner)

    def test_Metric(self):
        obj = self.getObject(Metric, self.dataMetric)
        self.checkFields(obj, self.dataMetric)

    def test_Imp(self):
        obj = self.getObject(Imp, self.dataImp)
        self.checkFields(obj, self.dataImp)

        self.assertIsInstance(obj.metric[0], Metric)
        self.assertIsInstance(obj.banner, Banner)
        self.assertIsInstance(obj.video, Video)
        self.assertIsInstance(obj.audio, Audio)
        self.assertIsInstance(obj.native, Native)
        self.assertIsInstance(obj.pmp, Pmp)

    def test_Source(self):
        self.assertOrtbFields(Source, self.dataSource)

    def test_Regs(self):
        self.assertOrtbFields(Regs, self.dataRegs)

    def test_BidRequest(self):
        obj = self.getObject(BidRequest, self.dataBidRequest)
        self.checkFields(obj, self.dataBidRequest)

        self.assertIsInstance(obj.imp[0], Imp)
        self.assertIsInstance(obj.site, Site)
        self.assertIsInstance(obj.app, App)
        self.assertIsInstance(obj.device, Device)
        self.assertIsInstance(obj.user, User)
        self.assertIsInstance(obj.source, Source)
        self.assertIsInstance(obj.regs, Regs)
