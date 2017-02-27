import os
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
<<<<<<< HEAD
=======
import django
>>>>>>> 8c1491d18f4e73764cf530977a890450c1ae945f

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
    'ldap_sync',
    'btp',
    'accounts',
    'gp',
    'feasta',
    'polls',
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

AUTH_LDAP_SERVER_URI = "ldap.iiits.in"


AUTH_LDAP_BIND_DN = "cn=django-agent,dc=iiits,dc=in"
AUTH_LDAP_BIND_PASSWORD = "iiits@123"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=people,dc=iiits,dc=in",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=people,dc=iiits,dc=in"

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=django,ou=groups,dc=iiits,dc=in",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=django,ou=groups,dc=iiits,dc=in"
AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=django,ou=groups,dc=iiits,dc=in"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_PROFILE_ATTR_MAP = {
    "employee_number": "employeeNumber"
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active,ou=django,ou=groups,dc=iiits,dc=in",
    "is_staff": "cn=staff,ou=django,ou=groups,dc=iiits,dc=in",
    "is_superuser": "cn=superuser,ou=django,ou=groups,dc=iiits,dc=in"
}

AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
    "is_awesome": "cn=awesome,ou=django,ou=groups,dc=iiits,dc=in",
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

<<<<<<< HEAD

=======
#LDAP SETTINGS

LDAP_SYNC_URI = "ldap://ldap.iiits.in"
LDAP_SYNC_BASE = "OU=people,DC=iiits,DC=in"
>>>>>>> 8c1491d18f4e73764cf530977a890450c1ae945f
# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True
<<<<<<< HEAD

=======
'''
>>>>>>> 8c1491d18f4e73764cf530977a890450c1ae945f
STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'staticfiles'),
    '/var/www/cosmosenv/cosmos/staticfiles/',
)
'''
SERVE_MEDIA = True
STATIC_URL = '/static/'
<<<<<<< HEAD
#STATIC_ROOT = '/var/www/cosmosenv/cosmos/staticfiles/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
=======
STATIC_ROOT = '/var/www/cosmosenv/cosmos/staticfiles/' #os.path.join(BASE_DIR, 'staticfiles')
>>>>>>> 8c1491d18f4e73764cf530977a890450c1ae945f
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

