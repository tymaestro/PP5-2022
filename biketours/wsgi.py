"""
WSGI config for biketours project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biketours.settings')

application = get_wsgi_application()
