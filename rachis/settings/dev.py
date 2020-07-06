import os
from os.path import dirname, join

from dotenv import load_dotenv

from .defaults import *

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",  
        "NAME": os.getenv("db_name"),
        "USER": os.getenv("db_user"),
        "PASSWORD": os.getenv("db_password"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}