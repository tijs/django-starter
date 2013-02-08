from __future__ import absolute_import
from .base import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MANAGERS = (
    ("The Team", "team@yourapp.com"), # You probably want to change this
    )

# This example uses database credentials from env vars, feel free to just put yours in there hardcoded
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ['DB_NAME'],                      # Or path to database file if using sqlite3.
        'USER': os.environ['DB_USERNAME'],                      # Not used with sqlite3.
        'PASSWORD': os.environ['DB_PASSWORD'],                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Change this to memcache if you have it!
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
}

# This should get you started, although you probably want to use Sendgrid, Mailgun or something similar
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'email@example.com' # change this to something that works