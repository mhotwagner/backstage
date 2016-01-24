from .base import *


MEDIA_ROOT = BASE_DIR.child("media")
STATIC_ROOT = BASE_DIR.child("static")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'megdev',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    BASE_DIR.child('static_source'),
)
