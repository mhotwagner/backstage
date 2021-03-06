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
MEDIA_URL = '/media/'

# Static file handling
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_source'),
)
