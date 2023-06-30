#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn dockerize.wsgi -b 0.0.0.0:${PORT}