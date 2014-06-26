from settings import *

DEBUG = True

#DATABASE_ENGINE = 'postgresql_psycopg2'
#DATABASE_NAME = 'abc_search'
#DATABASE_USER = 'root'
#DATABASE_PASSWORD = ''
#DATABASE_HOST = '192.168.0.10'
#DATABASE_PORT = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'abc_search',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '192.168.0.10',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
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
