from settings import *

DEBUG = True
DEV_MODE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'julian_s3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '192.168.0.10',
        'PORT': '',
    }
}


REGION_PROFILES_ADDON = True
BRANCH_LEVEL_ACCESS_ADDON = True
PORTALS_ADDON = True
COMMERCIAL_ADDON = True
HOLIDAY_ADDON = True
FACEBOOK_ADDON = True
DOCUMENTS_ADDON = True
NEW_DEVELOPMENT_ADDON = True
OFFERS_ADDON = True

WEBSITE_URL = "http://dev.int.propdata.net:24002"
SENTRY_DSN = None
S3_FOLDER_NAME = 'test'

#MOBI_URL = "http://127.0.0.1:8001"

#if MOBI_URL:
#    MIDDLEWARE_CLASSES += (
#        'eos.lib.mobi_middleware.MobiMiddleware',
#    )


PP_FEED_USERNAME = "propdatauser"
PP_FEED_PASSWORD = "smartcat"

# Uncomment below lines to run django debug toolbar - update INTERNAL_IPS with your own
#INSTALLED_APPS += ('debug_toolbar',)
#INTERNAL_IPS = ('127.0.0.1', '192.168.0.116',)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
ANALYTICS_ID = "UA-XXXX-XX"


RECAPTCHA_PUBLIC_KEY = "6LeVBQETAAAAACcHL0MLw-HL5KgE6jLykWQaK5IY"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

COMPRESS_PRECOMPILERS = []
COMPRESS_CSS_FILTERS = []
COMPRESS_JS_FILTERS = []
COMPRESS_YUI_BINARY = None