# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

import os

from settings import DATABASES

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = '/home/%s/src/git_checkouts/statementicator/statementicator.db' % os.environ['USER']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/home/%s/src/git_checkouts/static/' % os.environ['USER']
MEDIA_ROOT = '/home/%s/src/git_checkouts/media/' % os.environ['USER']

# EOF


