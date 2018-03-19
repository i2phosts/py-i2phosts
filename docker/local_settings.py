import os

ALLOWED_HOSTS = ['*']

if os.environ['DJANGO_ENV'] == 'prod':
    DEBUG = False
else:
    DEBUG = True

#STATIC_ROOT = '{0}/{1}'.format(os.environ['WEBAPPDIR'], 'pyi2phosts/static-common')
STATIC_ROOT = '/static'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ['DB_NAME'],                      # Or path to database file if using sqlite3.
        'USER': os.environ['DB_USER'],                      # Not used with sqlite3.
        'PASSWORD': os.environ['DB_PASS'],                  # Not used with sqlite3.
        'HOST': os.environ['DB_HOST'],                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = os.environ['TIME_ZONE']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

SITE_NAME = os.environ['SITE_NAME']
DOMAIN = os.environ['DOMAIN']
MY_B64 = os.environ['MY_B64']

# with None logs will go to stdout
LOG_FILE = None

LATEST_DAY_COUNT = 30
LATEST_HOSTS_COUNT = 40

EEPROXY_URL = os.environ['proxyurl']
