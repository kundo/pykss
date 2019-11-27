import os
import django
from django.conf import settings


def pytest_configure(config):
    PROJECT_ROOT = os.path.dirname(__file__)

    if not settings.configured:
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                },
            },
            DEBUG=False,
            INSTALLED_APPS=[
                'pykss.contrib.django',
            ],
            PROJECT_ROOT=PROJECT_ROOT,
            TEMPLATE_DEBUG=True,
            TEMPLATE_DIRS=[os.path.join(PROJECT_ROOT, 'tests', 'templates')],
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [os.path.join(PROJECT_ROOT, 'tests', 'templates')],
                    'APP_DIRS': True,
                    'OPTIONS': {
                    },
                },
            ]
        )

        if hasattr(django, 'setup'):
            django.setup()
