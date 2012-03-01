# -*- coding: utf-8 -*-
import os.path


_ = lambda s: s

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]
SITE_ID = 1

TEMPLATE_DEBUG = True
INTERNAL_IPS = (
    '127.0.0.1',
    '10.0.1.203',
    '62.220.4.138',
)

SERVER_EMAIL = 'admin@pb.io'
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME
ADMINS = (
    ('Philipp Bosch', 'hello@pb.io'),
)
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
PROJECT_STATIC_ROOT = os.path.join(PROJECT_ROOT, '..', 'static')
STATICFILES_DIRS = (
    PROJECT_STATIC_ROOT,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = "ZiqHzTteeTZRDsdwVOyijx22Hr3u1SZt"
ROOT_URLCONF = '%s.urls' % PROJECT_NAME
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'gunicorn',
    'south',
    'compressor',
    '%s.conversation' % PROJECT_NAME
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

COMPRESS = True
COMPRESS_ROOT = PROJECT_STATIC_ROOT
COMPRESS_URL = STATIC_URL
COMPRESS_OUTPUT_DIR = 'compressed'
