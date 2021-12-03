# Staging Server Settings
from .base import *

ALLOWED_HOSTS = ["damp-reaches-35001.herokuapp.com"]

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False

# middlewire third party
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

INSTALLED_APPS += ["blog.apps.BlogConfig"]

# Database Config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ddmcv1n92qdcn7",
        "USER": "mrfqbfccfmhihz",
        "PASSWORD": "dc16a413949697ece35873b55f81b61747f34633e9478bc681a13fd41bfcd746",
        "HOST": "ec2-34-194-119-178.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}


# REST FRAMEWORK CONFIG
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    **{"DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)},
}
