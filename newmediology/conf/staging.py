from .default import PROJECT_NAME

EMAIL_HOST = 'imap.gmail.com'
EMAIL_HOST_USER = 'test@pb.io'
EMAIL_HOST_PASSWORD = 'test3579'
EMAIL_USE_TLS = True

CACHE_BACKEND = 'dummy:///'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

COMPRESS_URL = STATIC_URL = 'http://cdn.newmediology.org.s3.amazonaws.com/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, '..', 'static.tmp')
# COMPRESS_ROOT = STATIC_ROOT = os.path.join(PROJECT_ROOT, '..', 'static.tmp')
COMPRESS_STORAGE = '%s.util.storage.CachedS3BotoStorage' % PROJECT_NAME
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
