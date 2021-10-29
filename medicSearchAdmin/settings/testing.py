import os
from .settings import *

DEBUG = True

SECRET_KEY = '123456TEST'

ALLOWED_HOSTS = []

DATABASES = {
    'default':{
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.sqlite3' , 
    }
}