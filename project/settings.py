import os
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env.str('HOST', 'checkpoint.devman.org'),
        'PORT': env.int('PORT', '5434'),
        'NAME': env.str('NAME', ''),
        'USER': env.str('USER', ''),
        'PASSWORD': env.str('PASSWORD', ''),
    }
}

SECRET_KEY = env.str('SECRET_KEY', 'REPLACE_ME')

DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = ['datacenter']
ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
