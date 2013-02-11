# Django settings for starter project.
from unipath import FSPath as Path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tijs Teulings', 'tijs@automatique.nl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
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
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

PROJECT_DIR = Path(__file__).absolute().ancestor(3)

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_DIR.child('static_root')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    str(PROJECT_DIR.child('static')),
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder', # django-compressor uses this to find stuff to compress
    )

# I keep all templates for all apps in a single root dir, your mileage may vary
TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
    )

# Make this unique, and don't share it with anybody.
# Created for you, else use something like this for a nice long key: http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.Sentry404CatchMiddleware', # Send 404 notifications to Sentry
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

# this is the default context processors list with the addition of the request processor
# which adds a handy {{ request.something }} context to your templates
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    )

ROOT_URLCONF = 'starter.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'starter.wsgi.application'

RAVEN_CONFIG = {
    'dsn': '', # your Sentry DSN URL goes here
    }

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django extras
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.comments',

    # Django Admin
    'django.contrib.admin',

    # Tools
    'south',
    'raven.contrib.django',
    'compressor',
    'easy_thumbnails',

    # Apps
    'starter' # your 'core' app
    #'some_other_app'

    )

# I just copied this from the Raven/Sentry examples
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
            },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        },
    }

# django-compressor, default filter settings are fine so this is all the config we need
COMPRESS_OFFLINE = True # make sure we get pre-compressed static files on production (looks at your DEBUG setting)
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'pyscss --no-compress --load-path=%s {infile} > {outfile}' % str(PROJECT_DIR.child('static').child('sass'))),
)