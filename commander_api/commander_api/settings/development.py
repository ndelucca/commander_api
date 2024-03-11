from commander_api.settings.base import *

DEBUG = True

INTERNAL_IPS = "127.0.0.1"

ALLOWED_HOSTS = []

INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
