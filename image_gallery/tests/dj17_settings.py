"""
These settings are used by the ``manage.py`` command.

With normal tests we want to use the fastest possible way which is an
in-memory sqlite database but if you want to create South migrations you
need a persistant database.

Unfortunately there seems to be an issue with either South or syncdb so that
defining two routers ("default" and "south") does not work.

"""
from image_gallery.tests.test_settings import *  # NOQA

SECRET_KEY = 'gw4*+4qop3vxslfc**6oxn7vfa)h$2g_i$nmm2*a2_5!_qi&ra'

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'image_gallery': 'image_gallery.migrations_django',
}

LANGUAGES = [
    ('en-us', 'English (United States)'),
]

INSTALLED_APPS.remove('cms.plugins.text')
