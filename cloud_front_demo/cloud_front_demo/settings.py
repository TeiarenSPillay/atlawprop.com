from eos.core_settings import *
from os import path

DEV_MODE = False

if DEV_MODE:
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG
CURRENT_DIRECTORY = path.abspath(path.join(path.dirname(__file__)))

# This controls the clients add-ons
COMMERCIAL_ADDON = True
RESIDENTIAL_ADDON = True
NEW_DEVELOPMENT_ADDON = True
HOLIDAY_ADDON = True
REGION_PROFILES_ADDON = True
PERMISSIONS_ADDON = True
PORTALS_ADDON = False
DOCUMENTS_ADDON = True
OFFERS_ADDON = True
UNDER_CONSTRUCTION = True
# FACEBOOK_ADDON = True
# FACEBOOK_BRANCH_IDS = [x, y, z]

### Site specifics ###
SERVER_EMAIL = 'django@propdata.net'
WEB_STATS = "http://elb-1.aws.propdata.net/cgi-bin/awstats.pl?config=PROPDATA_WEBSITE_BUILDER_PROJECT_URL.aws-staging.propdata.net"
WEBSITE_URL = "http://PROPDATA_WEBSITE_BUILDER_PROJECT_URL.aws-staging.propdata.net"
# MOBI_URL = ""
ALLOWED_HOSTS = ['.aws-staging.propdata.net']
SENTRY_SITE = "http://PROPDATA_WEBSITE_BUILDER_PROJECT_URL.aws-staging.propdata.net"
S3_FOLDER_NAME = 'PROPDATA_WEBSITE_BUILDER_PROJECT_S3_PATH'

#GMAPS_KEY  = "ABQIAAAAZ7M1Fg4tth4J3zE3SdNNGhQopxaNlSGf-D4ne8JrgGl4on9aCxR8lLOa8U7yfvsm-aaXkQRoyD8rlw" # *.abcrealestate.co.za
#RECAPTCHA_PUBLIC_KEY = '6LfyycISAAAAAB2PddDRop69fIS3nmk9iqLltHIs'
#RECAPTCHA_PRIVATE_KEY = '6LfyycISAAAAAIuVa0HI-P6WH_uCp88MG_aJ7TmF'

# Brochure colours - Format: [RED, GREEN, BLUE]
BROCHURE_TITLE_P1 = [0.82, 0.55, 0.0]  # Top heading - first part
BROCHURE_TITLE_P2 = [0.0, 0.0, 0.0]    # Top heading - second part
BROCHURE_DATE = [0.80, 0.80, 0.80]     # Date
BROCHURE_HEADINGS = [0.0, 0.0, 0.0]    # Section headings
BROCHURE_PRICE = [0.0, 0.0, 0.0]       # Price
BROCHURE_WEBSITE = [0.82, 0.55, 0.0]   # Website address (bottom)

# Sesson config
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = '172.16.20.42'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_PREFIX = CURRENT_DIRECTORY.split("/")[-1]

### Database details ###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PROPDATA_WEBSITE_BUILDER_PROJECT_DATABASE_NAME',
        'USER': 'PROPDATA_WEBSITE_BUILDER_PROJECT_USER_NAME',
        'PASSWORD': 'PROPDATA_WEBSITE_BUILDER_PROJECT_DATABASE_PASSWORD',
        'HOST': 'db-3.aws.propdata.net',
        'PORT': '',
    }
}

TIME_ZONE = 'Africa/Johannesburg'
SECRET_KEY = 'w2ny#2xq&6yn)ffow!%(g@ww2r)mi03^(f+un-8_0$h#i6xlv5'


#CLIENT_MIDDLEWARE = ()
if not DEV_MODE:
    ANALYTICS_ID = 'UA-XXXX'
    MIDDLEWARE_CLASSES += (
        'eos.lib.analytics.GoogleAnalyticsMiddleware',
        'eos.lib.mobi_middleware.MobiMiddleware',
    )

if UNDER_CONSTRUCTION:
    MIDDLEWARE_CLASSES += (
        'eos.lib.under_construction.UnderConstructionMiddleware',
    )

# ROOT_URLCONF = 'PROPDATA_WEBSITE_BUILDER_PROJECT_ROOT_URLCONF.urls'

# Uncomment below if you testing on template project
ROOT_URLCONF = 'cloud_front_demo.urls'

AGENT_PHOTO_SIZES.append("69x69")

# Static configs
MEDIA_ROOT = '%s/../assets' % CURRENT_DIRECTORY
STATIC_ROOT = "%s/../static" % CURRENT_DIRECTORY
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    path.join(CURRENT_DIRECTORY, '../assets'),
    path.join(EOS_DIRECTORY, 'assets'),
)

TEMPLATE_DIRS += (
    '%s/../html' % CURRENT_DIRECTORY,
)
