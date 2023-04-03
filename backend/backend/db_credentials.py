from enum import Enum


class DbCredentials(Enum):
    ENGINE = "django.db.backends.postgresql"
    NAME = "web_inventory_app"
    USER = "postgres"
    PASSWORD = "09pq!_2x"
    HOST = "127.0.0.1"
    PORT = "5432"
