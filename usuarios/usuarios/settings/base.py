from unipath import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'unyi3ntlztta1o_)kcwdbt=*$9f9dc_!oi!)+!n6jkn&oya4hv'


ROOT_URLCONF = 'usuarios.urls'


TEMPLATES = [
    {
        'BACKEND'   : 'django.template.backends.django.DjangoTemplates' ,
        'DIRS'      : [BASE_DIR.child('templates')]                     ,
        'APP_DIRS'  : True                                              ,
        'OPTIONS'   : {
            'context_processors': [
                'django.template.context_processors.debug'           ,
                'django.template.context_processors.request'         ,
                'django.contrib.auth.context_processors.auth'        ,
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'usuarios.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True