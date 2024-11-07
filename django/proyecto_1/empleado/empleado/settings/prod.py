from .base import *

DEBUG = True

ALLOWED_HOSTS = ['164.92.107.9', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bded5',
        'USER ': 'christian',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")