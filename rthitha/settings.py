# Django settings for rthitha project.
import os
from django.conf import global_settings
#import custompipe
#import os.path.dirname as d, sys.path as p; p.insert(0,d(d(__file__)))

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('rthitha', 'rthithacom@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': '',                      # Or path to database file if using sqlite3.
        # 'USER': '',                      # Not used with sqlite3.
        # 'PASSWORD': '',                  # Not used with sqlite3.
        # 'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '',                      # Set to empty string for default. Not used with sqlite3.

		# 'ENGINE': 'django.db.backends.mysql',
		# 'NAME': 'rthitha',
		# 'USER': 'django_user',
		# 'PASSWORD': 'thepassword'

		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'cizrage$rthitha',
		'USER': 'cizrage',
		'PASSWORD': 'ygmfromthuya',
		'HOST': 'mysql.server',
		'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.3/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.rthitha.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = 'http://127.0.0.1:8000/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = '/home/cizrage/rthitha/static'
# STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # "E:/Git/rthitha/static",
    # os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3&xj&!!zdb&*iw%=q27@$7=9#tl4w)l%rp0xyfsvqo-=&^8hpl'

# List of callables that know how to import templates from various sources.
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

ROOT_URLCONF = 'rthitha.urls'



TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # PROJECT_PATH + '/templates/',
    os.path.join(PROJECT_PATH, 'templates')
)

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
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'zmovies',
    'tvseries',
    'social_auth',
    'debug_toolbar',
)


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


SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'


AUTHENTICATION_BACKENDS = (
	'social_auth.backends.twitter.TwitterBackend',
	'social_auth.backends.facebook.FacebookBackend',
	'social_auth.backends.google.GoogleOAuthBackend',
	'social_auth.backends.google.GoogleOAuth2Backend',
	'social_auth.backends.google.GoogleBackend',
	'social_auth.backends.yahoo.YahooBackend',
	'social_auth.backends.browserid.BrowserIDBackend',
	'social_auth.backends.contrib.linkedin.LinkedinBackend',
	'social_auth.backends.contrib.disqus.DisqusBackend',
	'social_auth.backends.contrib.livejournal.LiveJournalBackend',
	'social_auth.backends.contrib.orkut.OrkutBackend',
	'social_auth.backends.contrib.foursquare.FoursquareBackend',
	'social_auth.backends.contrib.github.GithubBackend',
	'social_auth.backends.contrib.vk.VKOAuth2Backend',
	'social_auth.backends.contrib.live.LiveBackend',
	'social_auth.backends.contrib.skyrock.SkyrockBackend',
	'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
	'social_auth.backends.contrib.readability.ReadabilityBackend',
	'social_auth.backends.contrib.fedora.FedoraBackend',
	'social_auth.backends.OpenIDBackend',
	'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	'social_auth.context_processors.social_auth_by_type_backends',
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
)

#AUTH_USER_MODEL = 'zmovies.Employee'

SOCIAL_AUTH_PIPELINE = (
	'social_auth.backends.pipeline.social.social_auth_user',
	#'social_auth.backends.pipeline.associate.associate_by_email',
	'social_auth.backends.pipeline.user.get_username',
	'social_auth.backends.pipeline.user.create_user',
	'social_auth.backends.pipeline.social.associate_user',
	'social_auth.backends.pipeline.social.load_extra_data',
	'social_auth.backends.pipeline.user.update_user_details',
	'rthitha.pipeline.get_user_avatar',
)

#AUTH_PROFILE_MODULE= 'UserProfile'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

GOOGLE_OAUTH2_CLIENT_ID='310327175751-04b1pdvkbt2vcommadmbv2e881o0h5um.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET='B3mqNT8nipDN-J5lSkfN2Rs-'


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/private/'
LOGIN_ERROR_URL = '/login-error/'
LOGIN_ERROR_MESSAGE = True

try:
    from local_settings import *
except ImportError:
    print u'File local_settings.py is not found. Continuing with production settings.'

