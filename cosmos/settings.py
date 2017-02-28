import os
import ldap
from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType
import django
from pswd import LDAP_PASS, LDAP_USER

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1!8i+co^$n=k(8$(%0!k5z&dqnl#fog@b_#*!wekum(_*pi4x2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'markdown_deux',
    'pagedown',
    'comments',
    'posts',
    'ldap_sync',
    'btp',
    'accounts',
    'gp',
    'feasta',
    'polls',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'cosmos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),'/var/www/cosmosenv/cosmos/templates'],
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

WSGI_APPLICATION = 'cosmos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
django.setup()

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Binding and connection options
AUTH_LDAP_SERVER_URI = "ldap://10.0.1.3:389"
AUTH_LDAP_BIND_DN = LDAP_USER
AUTH_LDAP_BIND_PASSWORD = LDAP_PASS
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 1,
    ldap.OPT_REFERRALS: 0,
}

# User and group search objects and types
AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=people,DC=iiits,DC=in",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=people,DC=iiits,DC=in",
    ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Cache settings
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300

# What to do once the user is authenticated
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_FIND_GROUP_PERMS = True

# The backends needed to make this work.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend')



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
    '/var/www/cosmosenv/cosmos/staticfiles/'
)
'''
SERVE_MEDIA = True
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/cosmosenv/cosmos/staticfiles/' #os.path.join(BASE_DIR, 'staticfiles')
LOGIN_REDIRECT_URL = '/'
LOGIN_URL ='/accounts/login/'
LOGOUT_URL = LOGIN_REDIRECT_URL

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'btpc@iiits.in'
EMAIL_HOST_PASSWORD = 'btpc@987#'
ISSUE_EMAIL_HOST_USER = 'issues.suggestions@gmail.com'
ROOM_EMAIL_HOST_USER = 'roombookings@gmail.com'
ISSUE_EMAIL_HOST_PASSWORD = 'SEs=8gWh@b~:m&{m'
BOOKING_EMAIL_HOST_USER = 'room.bookings@gmail.com'
BOOKING_EMAIL_HOST_PASSWORD = 'room@iiits'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

