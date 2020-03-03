import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')mlpmxl2z&ku1-k7&!(pcv5#@a_*%w421f!_wd7cah1uw9h%m#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'core',
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Путь для статических файлов (css, js, img, fonts...)
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

# URL статических файлов
STATIC_URL = '/static/'

# Путь для статических файлов в разработке
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'assets'),
)

from datetime import timedelta
import djcelery


djcelery.setup_loader()

REDIS_BACKEND = {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0,
}

REDIS_BACKEND_URL = 'redis://{host}:{port}/{db}'.format(
    host=REDIS_BACKEND['HOST'],
    port=REDIS_BACKEND['PORT'],
    db=REDIS_BACKEND['DB'],
)


CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'

CELERY_TASK_RESULT_EXPIRES = 18000   # 5 часов

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

BROKER_URL = REDIS_BACKEND_URL

CELERYBEAT_SHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERYBEAT_SHEDULE = {
    'greet-every-5-seconds': {
        'task': 'testing_pizza.tasks.greet_new_orders',
        'schedule': timedelta(seconds=5),
    },
}
