import werkzeug.urls
from urllib.parse import quote, unquote, urlencode, parse_qsl

werkzeug.urls.url_quote = quote
werkzeug.urls.url_encode = urlencode

class DecodedURL(dict):
    def to_dict(self, flat=True):
        return dict(self)

def url_decode(s, charset='utf-8', **kwargs):
    if isinstance(s, bytes):
        s = s.decode(charset)
    return DecodedURL(parse_qsl(s))

werkzeug.urls.url_decode = url_decode
