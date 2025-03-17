"""
Django settings for cart project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = 'django-insecure-yg3@(tb*d#@*oq+v)2=h9w%dsc66_**^)&3zik$x8gbl)pbx@5'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
DEBUG = os.environ.get("DEBUG","False").lower == "true" 

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cartapp',
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

ROOT_URLCONF = 'cart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'cart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

database_url = os.environ.get("DATABASE_URL") 
# DATABASES["default"] = dj_database_url.parse(database_url)

DATABASES = {
    # 'default': dj_database_url.parse("postgresql://cart_517j_user:ZvzbQ2buEsGfHASskfodwEjZvHT65nL3@dpg-cvbnontds78s73amu820-a.oregon-postgres.render.com/cart_517j") 
    'default': dj_database_url.parse(database_url)
    #  'default': {
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': BASE_DIR / 'db.sqlite3',
#          #mySQL 
#         # 'ENGINE': 'django.db.backends.mysql', 
#         # 'NAME': 'cart', 
#         # 'USER': 'root', 
#         # 'PASSWORD': '1234', 
#         # 'HOST': 'localhost', 
#         # 'PORT': '8888', 
#         # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 
#         # 'charset': 'utf8mb4',
#         #  
#         #mariaDB
#         # 'ENGINE': 'django.db.backends.mysql', 
#         # 'NAME': 'cart', 
#         # 'USER': 'admin', 
#         # 'PASSWORD': '1234', 
#         # 'HOST': 'localhost', 
#         # 'PORT': '3306', 
#         # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 
#         # 'charset': 'utf8mb4', 
        

    #  }
 }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
