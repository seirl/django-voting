# coding: utf-8

from __future__ import unicode_literals

import os

DIRNAME = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

SECRET_KEY = 'foo'

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'voting',
    'test_app',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'voting.urls'
