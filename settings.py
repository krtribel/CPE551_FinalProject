from pathlib import Path
import os
# import dj_database_url  # error?
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y0!jo3x-i__o#e%i@*%dqn5qh+3cz_3_6j$rkqxx*$f&@+p-*f'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'user',
    'posts',
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

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'

# keep getting erro for incorrect database set up
DATABASES = {
    'default': {},
    'users': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swap_users',
        'USER': 'postgres',
        'PASSWORD': '1824',
        'HOST': 'localhost',
        'PORT': '5432',


    },
    'posts': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swap_posts',
        'USER': 'postgres',
        'PASSWORD': '1824',
        'HOST': 'localhost',
        'PORT': '5432',

    }

}

DATABASE_ROUTERS = []


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


STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'default_permission_classes': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'default_authentication_classes': [
        'rest_framework_simplejwt.authentication.JWTAuthenication',
    ]
}

SIMPLE_JWT = {
    'access_token_lifetime': timedelta(minutes=30),
    'fresh_token_lifetime': timedelta(days=1),
    'auth_header_types': ('Bearer', ),
    'auth_token_classes': ('rest_framework_simplejwt.tokens.AccessToken', )
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.UserAcc'
