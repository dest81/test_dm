import os, sys

_ = lambda s: s

_PATH = os.path.abspath(os.path.dirname(__file__))

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('basett'),                 # Or path to database
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
    )

#TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

#LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'ru-RU'
LANGUAGE_CODE = 'uk-UA'

LANGUAGES = (
    ('ua', _('Ukraine')),
    ('ru', _('Russian')),
    ('en', _('English')),
    )

TIME_ZONE = 'Europe/Kiev'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

#AUTH_PROFILE_MODULE = 'users.UserProfile'

MEDIA_ROOT = os.path.join(_PATH, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(_PATH, 'files', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/'


#ADMIN_MEDIA_PREFIX = rel('static')

#STATIC_ROOT = rel('static')
#STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#)

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Make this unique, and don't share it with anybody.
SECRET_KEY = 'in^1bmya(bxn!^3gh5s!vjf#gd_g8gr-y+an*sjl&@7kx8c9)n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

)

ROOT_URLCONF = 'test_dm.urls'

INTERNAL_IPS = ('127.0.0.1',)

#TEMPLATE_DIRS = ('C:/Users/Dest/PycharmProjects/registrationdj/templates',)
TEMPLATE_DIRS = (rel('templates'))

INSTALLED_APPS = (
    'south',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'test_dm.dynamic_models',

)

#AUTHENTICATION_BACKENDS = (
#    'taskmanagerbs.auth_backends.CustomUserModelBackend',
#    'django.contrib.auth.backends.ModelBackend',
#    'guardian.backends.ObjectPermissionBackend',
#    )

#ANONYMOUS_USER_ID = -1

#CUSTOM_USER_MODEL = 'task.CustomUser'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

