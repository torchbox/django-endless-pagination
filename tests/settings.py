"""Settings file for the Django project used for tests."""

import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


PROJECT_NAME = 'project'

# Base paths.
ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT = os.path.join(ROOT, PROJECT_NAME)

# Django configuration.
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}
DEBUG = TEMPLATE_DEBUG = True
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'endless_pagination',
    'nose',
    PROJECT_NAME,
)
LANGUAGE_CODE = os.getenv('ENDLESS_PAGINATION_LANGUAGE_CODE', 'en-us')
ROOT_URLCONF = PROJECT_NAME + '.urls'
SECRET_KEY = os.getenv('ENDLESS_PAGINATION_SECRET_KEY', 'secret')
SITE_ID = 1
STATIC_ROOT = os.path.join(PROJECT, 'static')
STATIC_URL = '/static/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT, 'templates')
        ],
        'OPTIONS': {
            'context_processors': list(TEMPLATE_CONTEXT_PROCESSORS) + [
                'django.template.context_processors.request',
                PROJECT_NAME + '.context_processors.navbar',
                PROJECT_NAME + '.context_processors.versions',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
            ]
        },
    }
]

# Testing.
NOSE_ARGS = (
    '--verbosity=2',
    '--with-coverage',
    '--cover-package=endless_pagination',
)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
