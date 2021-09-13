import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'DB_ENGINE': os.getenv("DB_ENGINE"),
        'DB_HOST': os.getenv("DB_HOST"),
        'DB_PORT': os.getenv("DB_PORT"),
        'DB_NAME': os.getenv("DB_NAME"),
        'DB_USER': os.getenv("DB_USER"),
        'DB_PASSWORD': os.getenv("DB_PASSWORD"),
    }
}

SECRET_KEY = os.getenv("SECRET_KEY")
INSTALLED_APPS = ['datacenter']

DEBUG = os.getenv("DEBUG")


ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


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
