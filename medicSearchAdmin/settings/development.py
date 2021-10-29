import os
from .settings import *
 
DEBUG = True

SECRET_KEY = '123456dev'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join (BASE_DIR, 'sqlite3'),
    }
}