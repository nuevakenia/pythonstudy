from pathlib import Path

_BASE_DIR = Path(__file__).resolve().parent.parent

DB_POSTGRESQL_LOCAL = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'study',
    'USER': 'postgres',
    'PASSWORD': '123',
    'HOST': 'localhost',
    'PORT': '5432',
}

DB_POSTGRESQL_PRODUCTIVO = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'study',
    'USER': 'postgres',
    'PASSWORD': '123',
    'HOST': 'localhost',
    'PORT': '5432',
}

DB_POSTGRESQL_DESARROLLO = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'study',
    'USER': 'postgres',
    'PASSWORD': '123',
    'HOST': 'localhost',
    'PORT': '5432',
}
