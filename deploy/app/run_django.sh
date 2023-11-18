#!/bin/sh

python "manage.py" collectstatic --noinput

python "manage.py" migrate --noinput

gunicorn -c "$PROJECT_ROOT/gunicorn.conf.py" backend.wsgi:application
