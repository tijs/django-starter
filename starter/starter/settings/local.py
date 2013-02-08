from __future__ import absolute_import
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MANAGERS = (
    ("Tijs Teulings", "tijs@automatique.nl"),
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'your_database',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Dummy backends are your friends (locally that is)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'