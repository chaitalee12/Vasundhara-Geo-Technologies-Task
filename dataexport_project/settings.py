import os 
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent 

SECRET_KEY = 'django-insecure-your-secret-key-here' 

DEBUG = True 

ALLOWED_HOSTS = [ ]

# Installed apps 
INSTALLED_APPS = [ 
'django.contrib.admin', 
'django.contrib.auth', 
'django.contrib.contenttypes', 
'django.contrib.sessions', 
'django.contrib.messages', 
'django.contrib.staticfiles', 
'export_app',   
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

ROOT_URLCONF = 'dataexport_project.urls' 

TEMPLATES = [ 
{ 
'BACKEND': 'django.template.backends.django.DjangoTemplates', 
'DIRS': [ ],   
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

WSGI_APPLICATION = 'dataexport_project.wsgi.application' 

# Database  
DATABASES = { 
'default': { 
'ENGINE': 'django.db.backends.sqlite3', 
'NAME': BASE_DIR / 'db.sqlite3', 
} 
} 

# Password validation 
AUTH_PASSWORD_VALIDATORS = [ 
{ 
}, 
{ 
'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', 
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
}, 
] 

# Internationalization 
LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'Asia/Kolkata' 
USE_I18N = True 
USE_TZ = True 

# Static files 
STATIC_URL = '/static/' 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 

# Email backend  
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
