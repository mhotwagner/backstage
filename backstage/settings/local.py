from .base import *

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


STATIC_ROOT = BASE_DIR.child("static")

# import scss
# scss.config.STATIC_ROOT = STATIC_ROOT


STATICFILES_DIRS = (
    BASE_DIR.child('static_source'),
)
