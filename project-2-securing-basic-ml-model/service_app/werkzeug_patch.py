import werkzeug.urls
# patch werkzeug.urls directly for flask_oauthlib compatibility
werkzeug.urls.url_quote = werkzeug.urls.quote
werkzeug.urls.url_decode = werkzeug.urls.unquote
werkzeug.urls.url_encode = werkzeug.urls.urlencode
