import os

import dj_database_url

from .base import *

DEBUG = False

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config()
}

# Media handling
MEDIA_ROOT = BASE_DIR.child("media")

# Static file handling
STATIC_ROOT = 'static_sources'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
