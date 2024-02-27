"""
WSGI config for commander_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# wsgi for pythonanywhere.com

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/ndelucca/dev/commander_api"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "commander_api.settings.production")

application = get_wsgi_application()
