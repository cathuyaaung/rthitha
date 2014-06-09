import os
from django.conf import global_settings

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'rthitha',
		'USER': 'django_user',
		'PASSWORD': 'thepassword'
    }
}


DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (    
	'E:/Git/rthitha16/rthitha/static',	
)

ALLOWED_HOSTS = ['*',]