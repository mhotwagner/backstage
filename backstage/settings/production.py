import os

import dj_database_url

from .base import *

DEBUG = False

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config()
}


# Static file handling
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_source'),
)

# Media handling
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
