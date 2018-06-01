from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['anth-site.herokuapp.com']

try:
    from .local import *
except ImportError:
    pass
