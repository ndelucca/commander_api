from commander_api.settings.base import *

DEBUG = True
SECRET_KEY = "django-insecure-z6#5cp9f%fkx(8y13vk_vxm3ubydf^a)=@^z$*3r)fum6i2vbw"
ALLOWED_HOSTS = []
INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
