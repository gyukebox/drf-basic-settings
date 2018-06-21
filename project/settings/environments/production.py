import os
from project.settings import BASE_DIR

DEBUG = False

# Modify ALLOWED_HOSTS to appropriate hosts
ALLOWED_HOSTS = ['*.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
