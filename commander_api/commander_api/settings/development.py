from commander_api.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
