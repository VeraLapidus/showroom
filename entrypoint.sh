#!/bin/bash

sleep 10

# Collect static files
echo "Collect static files"
python manage.py collectstatic --no-input

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn my_showroom.wsgi:application --bind 0.0.0.0:8000
#python manage.py runserver 0.0.0.0:8000

exec "$@"