import os.path

from .default import PROJECT_ROOT, PROJECT_NAME

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT_NAME,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DISABLED_APPS = (
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '..', 'media')

EMAIL_HOST = 'imap.gmail.com'
EMAIL_HOST_USER = 'test@pb.io'
EMAIL_HOST_PASSWORD = 'test3579'
EMAIL_USE_TLS = True

CACHE_BACKEND = 'dummy:///'
