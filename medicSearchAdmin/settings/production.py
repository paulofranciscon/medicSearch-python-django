import os
from .settings import *

DEBUG = False

SECRET_KEY = '123456PROD'

ALLOWED_HOSTS = []

DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db,sqlite3'),

    }
}