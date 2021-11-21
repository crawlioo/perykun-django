# Staging Server Settings
from .base import *

ALLOWED_HOSTS = ['damp-reaches-35001.herokuapp.com', '127.0.0.1:8000']

DEBUG = False

# middlewire third party
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

INSTALLED_APPS += ["blog.apps.BlogConfig"]

# Database Config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
