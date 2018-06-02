from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['anth-site.herokuapp.com']

AWS_ACCESS_KEY = config('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'anthsite'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_LOCATION = 'static'

STATIC_URL = 'https:''%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


try:
    from .local import *
except ImportError:
    pass
