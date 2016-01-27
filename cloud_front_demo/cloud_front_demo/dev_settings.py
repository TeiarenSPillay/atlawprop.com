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
UNDER_CONSTRUCTION = False

WEBSITE_URL = "http://dev.int.propdata.net:24011"
SENTRY_DSN = None
S3_FOLDER_NAME = 'test'
FACEBOOK_BRANCH_IDS = [925]

MOBI_URL = "http://m.dev.int.propdata.net:24011"

if MOBI_URL:
    MIDDLEWARE_CLASSES += (
        'eos.lib.mobi_middleware.MobiMiddleware',
    )

if UNDER_CONSTRUCTION:
    MIDDLEWARE_CLASSES += (
        'eos.lib.under_construction.UnderConstructionMiddleware',
    )

PP_FEED_USERNAME = "propdatauser"
PP_FEED_PASSWORD = "smartcat"

# Uncomment below lines to run django debug toolbar - update INTERNAL_IPS with your own
#INSTALLED_APPS += ('debug_toolbar',)
#INTERNAL_IPS = ('127.0.0.1', '192.168.0.116',)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
MIDDLEWARE_CLASSES += (
    'eos.lib.analytics.GoogleAnalyticsMiddleware',
)
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

#PACKAGE_OPTION = "Lite"

#if PACKAGE_OPTION == 'Lite':
#    RESIDENTIAL_ADDON = True
#    COMMERCIAL_ADDON = False
#    NEW_DEVELOPMENT_ADDON = False
#    HOLIDAY_ADDON = False
#    PORTALS_ADDON = False
#    REGION_PROFILES_ADDON = False
#    OFFERS_ADDON = False
#    CUSTOM_NEWSLETTER_ADDON = False
#    LIST_YOUR_PROPERTY_DISPLAY = False
