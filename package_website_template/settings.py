from eos.core_settings import *
from os import path

DEV_MODE = False

if DEV_MODE:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG
CURRENT_DIRECTORY = path.abspath(path.dirname(__file__))

### Site specifics ###
SERVER_EMAIL = 'django@propdata.net'
WEB_STATS    = "http://unconfigured.propdata.net/cgi-bin/awstats.pl?config=unconfigured.co.za"
WEBSITE_URL  = "http://unconfigured.propdata.net"

# Brochure colours - Format: [RED, GREEN, BLUE]
BROCHURE_TITLE_P1 = [0.82, 0.55, 0.0]   # Top heading - first part
BROCHURE_TITLE_P2 = [0.0, 0.0, 0.0]     # Top heading - second part
BROCHURE_DATE     = [0.80, 0.80, 0.80]  # Date
BROCHURE_HEADINGS = [0.0, 0.0, 0.0]     # Section headings
BROCHURE_PRICE    = [0.0, 0.0, 0.0]     # Price
BROCHURE_WEBSITE  = [0.82, 0.55, 0.0]   # Website address (bottom)

# Client add-ons

# Production DB Settings
DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'unconfigured'          # Or path to database file if using sqlite3.
DATABASE_USER = 'unconfigured'          # Not used with sqlite3.
DATABASE_PASSWORD = 'unconfigured'      # Not used with sqlite3.
DATABASE_HOST = 'localhost'         # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''                      # Set to empty string for default. Not used with sqlite3.

# Production API Keys
#GMAPS_KEY  = "unconfigured"  # mydomain.co.za
#RECAPTCHA_PUBLIC_KEY = 'unconfigured'  # mydomain.co.za
#RECAPTCHA_PRIVATE_KEY = 'unconfigured'  # mydomain.co.za

TIME_ZONE = 'Africa/Johannesburg'
SECRET_KEY = 'w2ny#2xq&6yn)ffow!%(g@ww2r)mi03^(f+un-8_0$h#i6xlv5'

#if not DEV_MODE:
#    ANALYTICS_ID = 'UA-XXXX-XX'
#    MIDDLEWARE_CLASSES += (
#        'eos.lib.analytics.GoogleAnalyticsMiddleware',
#    )

MEDIA_ROOT = '%s/assets' % CURRENT_DIRECTORY
ROOT_URLCONF = 'package_website_template.urls'

TEMPLATE_DIRS += (
    '%s/html' % CURRENT_DIRECTORY,
)
