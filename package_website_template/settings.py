from eos.core_settings import *
from os import path

DEV_MODE = True

if DEV_MODE:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG
CURRENT_DIRECTORY = path.abspath(path.dirname(__file__))

### Site specifics ###
SERVER_EMAIL = 'unconfigured@propdata.net'
WEB_STATS    = "http://ws01.umh.propdata.net/cgi-bin/awstats.pl?config=unconfigured.co.za"
WEBSITE_URL  = "http://www.unconfigured.co.za"

# Brochure colours - Format: [RED, GREEN, BLUE]
BROCHURE_TITLE_P1 = [0.82, 0.55, 0.0]   # Top heading - first part
BROCHURE_TITLE_P2 = [0.0, 0.0, 0.0]     # Top heading - second part
BROCHURE_DATE     = [0.80, 0.80, 0.80]  # Date
BROCHURE_HEADINGS = [0.0, 0.0, 0.0]     # Section headings
BROCHURE_PRICE    = [0.0, 0.0, 0.0]     # Price
BROCHURE_WEBSITE  = [0.82, 0.55, 0.0]   # Website address (bottom)

# This controls the clients add-ons
COMMERCIAL_ADDON = True
NEW_DEVELOPMENT_ADDON = True
REGION_PROFILES_ADDON = True
BRANCH_LEVEL_ACCESS_ADDON = True

### Database details ###
if DEV_MODE:
    DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'unconfigured'          # Or path to database file if using sqlite3.
    DATABASE_USER = 'root'                  # Not used with sqlite3.
    DATABASE_PASSWORD = ''                  # Not used with sqlite3.
    DATABASE_HOST = '192.168.0.10'          # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''                      # Set to empty string for default. Not used with sqlite3.
    GMAPS_KEY  = "ABQIAAAAkzGFPn2aXs-JhTpG4AIIORRpp2cC2FsRFUfKRDdI-3JIXl2s9BRxtJbBjImxjaIlIespam7WOi-8ag" # localhost
else:
    DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'unconfigured'          # Or path to database file if using sqlite3.
    DATABASE_USER = 'unconfigured'          # Not used with sqlite3.
    DATABASE_PASSWORD = 'unconfigured'      # Not used with sqlite3.
    DATABASE_HOST = '196.37.205.41'         # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''                      # Set to empty string for default. Not used with sqlite3.
    GMAPS_KEY  = "unconfigured" # unconfigured.co.za
    #RECAPTCHA_PUBLIC_KEY = 'unconfigured'
    #RECAPTCHA_PRIVATE_KEY = 'unconfigured'

TIME_ZONE = 'Africa/Johannesburg'
SECRET_KEY = 'w2ny#2xq&6yn)ffow!%(g@ww2r)mi03^(f+un-8_0$h#i6xlv5'

#if not DEV_MODE:
#    ANALYTICS_ID = 'UA-13148074-26'
#    MIDDLEWARE_CLASSES += (
#        'eos.lib.analytics.GoogleAnalyticsMiddleware',
#    )

MEDIA_ROOT = '%s/assets' % CURRENT_DIRECTORY
ROOT_URLCONF = 'unconfigured.urls'

TEMPLATE_DIRS += (
    '%s/html' % CURRENT_DIRECTORY,
)
