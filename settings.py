# Django settings for buzzforbid project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_DIR = os.path.abspath(os.path. dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'buzzforbid',                      # Or path to database file if using sqlite3.
        'USER': 'riza',                      # Not used with sqlite3.
        'PASSWORD': '220281',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Jakarta'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

# ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'x$)m(kosg4eumn@a_+yv%^#!wax7rz2j(hdh^#zwusve89fup#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'buzzforbid.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates/')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',

    # Third Parties
    'django_extensions',
    'debug_toolbar',
    'tastypie',
    # 'south',
    'registration',

    # Our own models register
    'hotel',
    'geographic_info',
    'user_level',
    'room_type',
    'tour_request',
    'travel_agent',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Grappelli Setting
GRAPPELLI_ADMIN_TITLE = 'BuzzForbid Admin Site'
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)
# GRAPPELLI_INDEX_DASHBOARD = 'buzzforbid.dashboard.CustomIndexDashboard'


# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# DEFAULT_FROM_EMAIL = 'Buzzforbid Tour <tour@buzzforbid.com>'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Buzzforbid Tour <tour@buzzforbid.com>'
EMAIL_HOST_USER = 'rizafahmi@gmail.com'
EMAIL_HOST_PASSWORD = 'diyah02071982'

ACCOUNT_ACTIVATION_DAYS = 2
LOGIN_REDIRECT_URL = '/'
