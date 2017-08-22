# -*- coding: utf-8 -*-

###############################################
# Geosite local settings
###############################################

# path for static and uploaded files
SERVE_PATH = '{{ root_path }}'

# database info
DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'geonode'
DATABASE_USER = 'geonode'
DATABASE_PASSWORD = '6noUribZ'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode_data',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

# email account for sending email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#REGISTRATION_OPEN=True
#ACCOUNT_EMAIL_CONFIRMATION_EMAIL=True
#ACCOUNT_EMAIL_CONFIRMATION_REQUIRED=True

# uncomment for production
# PROXY_ALLOWED_HOSTS = ('.{{ domain }}')

# localhost by default
# GEOSERVER_URL = 'http://localhost:8080/'

ALLOWED_HOSTS = ['geonode.geonode.org',]
