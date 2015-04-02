from eos.core_settings import *
from os import path

DEV_MODE = False

if DEV_MODE:
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG
CURRENT_DIRECTORY = path.abspath(path.join(path.dirname(__file__), '..'))

### Site specifics ###
SERVER_EMAIL = 'django@propdata.net'
WEB_STATS    = "http://elb-1.aws.propdata.net/cgi-bin/awstats.pl?config=cloudfront-demo.aws-staging.propdata.net"
WEBSITE_URL  = "http://cloudfront-demo.aws-staging.propdata.net"

# Brochure colours - Format: [RED, GREEN, BLUE]
BROCHURE_TITLE_P1 = [0.82, 0.55, 0.0] # Top heading - first part
BROCHURE_TITLE_P2 = [0.0, 0.0, 0.0] # Top heading - second part
BROCHURE_DATE     = [0.80, 0.80, 0.80] # Date
BROCHURE_HEADINGS = [0.0, 0.0, 0.0] # Section headings
BROCHURE_PRICE    = [0.0, 0.0, 0.0] # Price
BROCHURE_WEBSITE  = [0.82, 0.55, 0.0] # Website address (bottom)

# This controls the clients add-ons
COMMERCIAL_ADDON = True
NEW_DEVELOPMENT_ADDON = True
HOLIDAY_ADDON = True
REGION_PROFILES_ADDON = True
PERMISSIONS_ADDON = True
PORTALS_ADDON = True
DOCUMENTS_ADDON = True
OFFERS_ADDON = True
WINDOW_DISPLAY_ADDON = {
    'residential': True,
    'commercial': True,
    'holiday': False,
    'new-developments': False
}
FACEBOOK_ADDON = True
FACEBOOK_BRANCH_IDS = [5376]
### Database details ###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cloudfront_demo',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'durr_estates',
        'PASSWORD': 'ujl8rse5zw',
        'HOST': 'db-1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
#GMAPS_KEY  = "ABQIAAAAZ7M1Fg4tth4J3zE3SdNNGhQopxaNlSGf-D4ne8JrgGl4on9aCxR8lLOa8U7yfvsm-aaXkQRoyD8rlw" # *.abcrealestate.co.za
#RECAPTCHA_PUBLIC_KEY = '6LfyycISAAAAAB2PddDRop69fIS3nmk9iqLltHIs'
#RECAPTCHA_PRIVATE_KEY = '6LfyycISAAAAAIuVa0HI-P6WH_uCp88MG_aJ7TmF'

S3_FOLDER_NAME = 'test'

ALLOWED_HOSTS = ['.aws-staging.propdata.net']

TIME_ZONE = 'Africa/Johannesburg'
SECRET_KEY = 'w2ny#2xq&6yn)ffow!%(g@ww2r)mi03^(f+un-8_0$h#i6xlv5'

ANALYTICS_ID = 'UA-13148074-26'

MIDDLEWARE_CLASSES += (
    'eos.lib.analytics.GoogleAnalyticsMiddleware',
)

ROOT_URLCONF = 'cloud_front_demo.urls'

# Static configs
MEDIA_ROOT = '%s/assets' % CURRENT_DIRECTORY
STATIC_ROOT = "%s/static" % CURRENT_DIRECTORY
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    path.join(CURRENT_DIRECTORY, 'assets'),
    path.join(EOS_DIRECTORY, 'assets'),
)

TEMPLATE_DIRS += (
    '%s/html' % CURRENT_DIRECTORY,
)

#SENTRY_SITE = "abcrealestate.co.za"
