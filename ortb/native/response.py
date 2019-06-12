
from ortb.core import Serializable


class NativeAdCreative(Serializable):
    """Native Ad Creative"""

    def __init__(self, args={}):
        # Required
        self.native = args['native'] if 'native' in args else None
        """Top level Native object"""


class Native(Serializable):
    """Native object"""

    # Required
    assets = []
    """List of native ad’s assets."""

    link = None
    """ Destination Link. This is default link object for the ad.
        Individual assets can also have a link object which applies
        if the asset is activated (clicked).
        If the asset doesn’t have a link object, the parent link object applies.
        See LinkObject Definition
    """

    # Optional
    ver = 1
    """Version of the Native Markup version in use."""

    imptrackers = []
    """ Array of impression tracking URLs, expected to return a 1x1 image or 204 response -
        typically only passed when using 3rd party trackers."""

    jstracker = None
    """ Optional JavaScript impression tracker.
        This is a valid HTML, Javascript is already wrapped in <script> tags.
        It should be executed at impression time where it can be supported."""

    ext = None
    """Placeholder for exchange-specific extensions to OpenRTB"""

    def __init__(self, args={}):
        for key, val in args.items():
            if 'link' == key:
                self.link = Link(val)
            elif 'assets' == key:
                self.assets = []
                for asset in val:
                    self.assets.append(Asset(asset))
            else:
                setattr(self, key, val)


class Asset(Serializable):
    """Asset object. Asset object may contain only one of title, img, data or video."""

    # Required
    id = None
    """Unique asset ID, assigned by exchange, must match one of the asset IDs in request"""

    # Optional
    required = 0
    """Set to 1 if asset is required."""

    title = None
    """Title object for title assets. See Title Object definition."""

    img = None
    """Image object for image assets. See Image Object definition."""

    video = None
    """ Video object for video assets. See Video Object definition.
        Note that in-stream video ads are not part of Native.
        Native ads may contain a video as the ad creative itself.
    """

    data = None
    """Data object for ratings, prices etc."""

    link = None
    """ Link object for call to actions. The link object applies
        if the asset item is activated (clicked).
        If there is no link object on the asset, the parent link object on the bid response applies.
    """

    ext = None
    """ Placeholder for exchange-specific extensions to OpenRTB.
        Bidders are encouraged not to use asset.ext for exchanging text assets.
        Use data.ext with custom type instead.
    """

    def __init__(self, args={}):
        for key, val in args.items():
            if 'title' == key:
                self.title = Title(val)
            elif 'img' == key:
                self.img = Image(val)
            elif 'video' == key:
                self.video = Video(val)
            elif 'data' == key:
                self.data = Data(val)
            elif 'link' == key:
                self.link = Link(val)
            else:
                setattr(self, key, val)


class Title(Serializable):
    """Title object"""

    # Required
    text = None
    """The text associated with the text element."""

    # Optional
    ext = None
    """Placeholder for exchange-specific extensions to OpenRTB"""

    def __init__(self, args={}):
        for key, val in args.items():
            setattr(self, key, val)


class Image(Serializable):
    """Image object"""

    # Required
    url = None
    """URL of the image asset."""

    # Recommended
    w = None
    """Width of the image in pixels."""

    h = None
    """Height of the image in pixels."""

    # Optional
    ext = None
    """Placeholder for exchange-specific extensions to OpenRTB"""

    def __init__(self, args={}):
        for key, val in args.items():
            setattr(self, key, val)


class Data(Serializable):
    """Data object"""

    # Required
    value = None
    """ The formatted string of data to be displayed.
        Can contain a formatted value such as “5 stars” or “$10” or “3.4 stars out of 5”
    """

    # Optional
    label = None
    """The optional formatted string name of the data type to be displayed."""

    ext = None
    """Placeholder for exchange-specific extensions to OpenRTB"""

    def __init__(self, args={}):
        for key, val in args.items():
            setattr(self, key, val)


class Video(Serializable):
    """ Video object. Corresponds to the Video Object in the request,
        yet containing a value of a conforming VAST tag as a value.
    """

    # Required
    vasttag = None
    """VAST xml."""

    def __init__(self, args={}):
        for key, val in args.items():
            setattr(self, key, val)


class Link(Serializable):
    """Used for ‘call to action’ assets, or other links from the Native ad.
    This Object should be associated to its peer object in the parent Asset Object or
    as the master link in the top level Native Ad response object.
    When that peer object is activated (clicked) the action should take the user
    to the location of the link.
    """

    # Required
    url = None
    """Landing URL of the clickable link."""

    # Optional
    clicktrackers = []
    """List of third-party tracker URLs to be fired on click of the URL."""

    fallback = None
    """ Fallback URL for deeplink.
        To be used if the URL given in url is not supported by the device.
    """

    ext = None
    """Placeholder for exchange-specific extensions to OpenRTB"""

    def __init__(self, args={}):
        for key, val in args.items():
            setattr(self, key, val)
