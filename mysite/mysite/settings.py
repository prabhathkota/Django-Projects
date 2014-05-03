# Django settings for mysite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'tiger',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

DEFAULT_CHARSET = 'utf-8'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# Set the STATIC_ROOT setting to the directory from which you'd like to serve these files, for example:
# STATIC_ROOT = "/var/www/example.com/static/"
# Run the collectstatic management command:
# ./manage.py collectstatic
# This will copy all files from your static folders into the STATIC_ROOT directory.
STATIC_ROOT = ''


# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # Don't forget to give comma at the end
	#Your project will probably also have static assets that aren't tied to a particular app. In addition to using a static/ directory inside your apps, you can define a list of directories (STATICFILES_DIRS) in your settings file where Django will also look for static files
    #E.g.,
    #os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
    'C:/Prabhath/django_workspace/mysite/mysite/contacts/templates/static/contacts',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@-k-1yjpo4&0qgil#qu^y697e2vwbkf_l&^*dc)-q&($shdok7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #manages sessions across requests
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #associates users with requests using sessions
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'C:/Prabhath/django_workspace/mysite/mysite/templates',
	'C:/Prabhath/django_workspace/mysite/mysite/books/templates',
	#'C:/Prabhath/django_workspace/mysite/mysite/books/templates/about',
	'C:/Prabhath/django_workspace/mysite/mysite/books/contact/templates',
	'C:/Prabhath/django_workspace/mysite/mysite/polls/templates',
	#os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'), #Dynamic URLs
)

#This will be not there by default in Settings.py
#I added after reading the docs
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'mysite.context_processors.custom_proc_outside', #I defined, its in mysite/context_processors.py, inside that custom_proc_outside method
)

INSTALLED_APPS = (
    'django.contrib.auth', #contains the core of the authentication framework, and its default models.
    'django.contrib.contenttypes', #is the Django content type system, which allows permissions to be associated with models you create.
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'envelope',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
	'mysite.books',
    'mysite.polls',
    'mysite.contacts',
    'tastypie',
    'oauth2_provider',
    'corsheaders',
)

#LOGIN_URL = '/accounts/login/'
#LOGIN_REDIRECT_URL = '/accounts/profile/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

#SMTP/Email Configurations
#DEFAULT_FROM_EMAIL = 'prabhathkota@gmail.com'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

#CORS - Cross-Origin Resource Sharing (CORS)
#This is part of django-cors-headers python module
#This will allow the public users to access your API/URLs
CORS_ORIGIN_ALLOW_ALL = True