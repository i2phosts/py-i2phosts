# Django settings for web project.

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u*x8(m=px4az@g+!-c&p9d5z0$g+bhw@t28wf*fz#lo$@^bc5u'

# Static files will be addressed as http://example.com/static/
STATIC_URL = '/static/'

# Additional dirs to look for static files. See https://docs.djangoproject.com/en/1.5/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "pyi2phosts/static-common"),
)

# Directories where Django looks for translation files
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "pyi2phosts/locale"),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware'
)

ROOT_URLCONF = 'pyi2phosts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pyi2phosts/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pyi2phosts.context_processors.global_settings',
                ]
        }
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'django.contrib.staticfiles',
    'pyi2phosts.postkey.apps.PostkeyConfig',
    'pyi2phosts.extsources.apps.ExtsourcesConfig',
)


# template for local settings:
"""
SECRET_KEY = 'topsecret'
SITE_NAME = 'My cool registration service'
DOMAIN = 'example.i2p'
MY_B64 = 'my_base64_hash'

"""
# also may be put in local settings:
LOG_LEVEL = 'debug'
LOG_FILE = '/var/log/py-i2phosts/web.log'
LATEST_DAY_COUNT = 30
LATEST_HOSTS_COUNT = 40
EEPROXY_URL = 'http://127.0.0.1:4444'


# include local settings
try:
    from local_settings_devel import *
except ImportError:
    pass
try:
    from local_settings import *
except ImportError:
    pass
