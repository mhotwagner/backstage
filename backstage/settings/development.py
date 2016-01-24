import os

import dj_database_url

from .base import *

DEBUG = True
DATABASE_URL = os.environ.get('DATABASE_URL')


DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = 'static'
