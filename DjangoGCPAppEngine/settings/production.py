from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": config("PROD_DB_ENGINE"),
        "HOST": config("PROD_DB_HOST"),
        "NAME": config("PROD_DB_NAME"),
        "USER": config("PROD_DB_USERNAME"),
        "PASSWORD": config("PROD_DB_PASSWORD"),
    }
}
