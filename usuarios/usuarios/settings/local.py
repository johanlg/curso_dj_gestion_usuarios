from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    'django.contrib.admin'          ,
    'django.contrib.auth'           ,
    'django.contrib.contenttypes'   ,
    'django.contrib.sessions'       ,
    'django.contrib.messages'       ,
    'django.contrib.staticfiles'    ,
]

LOCAL_APPS = [
    'applications.users',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware'             ,
    'django.contrib.sessions.middleware.SessionMiddleware'      ,
    'django.middleware.common.CommonMiddleware'                 ,
    'django.middleware.csrf.CsrfViewMiddleware'                 ,
    'django.contrib.auth.middleware.AuthenticationMiddleware'   ,
    'django.contrib.messages.middleware.MessageMiddleware'      ,
    'django.middleware.clickjacking.XFrameOptionsMiddleware'    ,
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : get_secret('DB_NAME')                   ,
        'USER'     : get_secret('USER')                      ,
        'PASSWORD' : get_secret('PASSWORD')                  ,
        'HOST'     : 'localhost'                             ,
        'PORT'     : '5432'                                  ,

    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL       = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static'),]

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')