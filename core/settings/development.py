from .base import *

INSTALLED_APPS += [
    'blog.apps.BlogConfig'
]

# Database Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}