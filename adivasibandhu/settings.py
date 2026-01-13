from pathlib import Path
import mimetypes

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*s8zsh2%h45j5_6bdt3lj50)4g+u!e88xoovck=s9e#rn@3lsg'

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '192.168.1.55',
]

# ------------------------------
# APPLICATIONS
# ------------------------------

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

# ------------------------------
# MIDDLEWARE
# ------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------
# URL / TEMPLATES
# ------------------------------

ROOT_URLCONF = 'adivasibandhu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------
# ASGI + WSGI
# ------------------------------

WSGI_APPLICATION = 'adivasibandhu.wsgi.application'
ASGI_APPLICATION = 'adivasibandhu.asgi.application'

# ------------------------------
# CHANNELS (DEV)
# ------------------------------

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}

# ------------------------------
# DATABASE
# ------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------
# PASSWORD VALIDATION
# ------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# INTERNATIONALIZATION
# ------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# STATIC FILES (FIXED)
# ------------------------------

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'main/static',
]

STATIC_ROOT = r'C:\Users\divya\OneDrive\Desktop\ADIVASI-DJANGO-APP\adivasibandhu\static'

# ------------------------------
# MEDIA FILES (FIXED)
# ------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = r'C:\Users\divya\OneDrive\Desktop\ADIVASI-DJANGO-APP\adivasibandhu\media'

# ------------------------------
# DEFAULTS
# ------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------
# EMAIL CONFIG
# ------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'divyanshrajshrivastava@gmail.com'
EMAIL_HOST_PASSWORD = 'dyrzlzdbuvwqbeus'
DEFAULT_FROM_EMAIL = 'divyanshrajshrivastava@gmail.com'

# ------------------------------
# CSRF / PROXY
# ------------------------------

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://192.168.1.55:9001',
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

# ------------------------------
# PWA MIME FIX
# ------------------------------

mimetypes.add_type('application/manifest+json', '.json', True)
