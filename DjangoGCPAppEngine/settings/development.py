from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": config("DEV_DB_ENGINE"),
        "HOST": config("DEV_DB_IP"),
        "NAME": config("DEV_DB_NAME"),
        "USER": config("DEV_DB_USERNAME"),
        "PASSWORD": config("DEV_DB_PASSWORD"),
    }
}
