"""
Django settings for markino project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'f4k3')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Email settings
DEFAULT_FROM_EMAIL = 'mail@mail.com'
SERVER_EMAIL = 'mail@mail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.host.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mail@mail.com'
EMAIL_HOST_PASSWORD = 'pass'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'huey.contrib.djhuey',
    'main',
    'phonenumber_field'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'markino.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'markino.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'handyman'),
        'USER': os.environ.get('POSTGRES_USER', 'root'),
        'PASSWORD':os.environ.get('POSTGRES_PASSWORD', 'admin'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = "main.LotrekUser"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Broker settings.
BROKER_URL = 'redis://localhost:6379'

# Testing

TESTING_SCHEDULE = {
    'hour' : '*',
    'minute' : '*',
    'day_of_week' : '*'
}

# Backup

BACKUP_FOLDER = 'backup_markino'

# BACKUP_SCHEDULE = {
#     'hour' : '13, 20',
# }

BACKUP_SCHEDULE = {
    'hour' : '*',
    'minute' : '*',
    'day_of_week' : '*'
}

BACKUP_PATH = os.path.join(BASE_DIR, BACKUP_FOLDER)

from huey import RedisHuey
from redis import ConnectionPool

pool = ConnectionPool(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379, max_connections=20)
HUEY = RedisHuey('handymantasks', connection_pool=pool)

try:
    from .local_settings import *
except ImportError:
    print ("\n\nWARNING: No local_settings.py found! Please look at the README.md file!\n\n")

try:
    os.makedirs(BACKUP_PATH)
except OSError:
    print('Backup Directory: {0} already exists!'.format(BACKUP_PATH))
