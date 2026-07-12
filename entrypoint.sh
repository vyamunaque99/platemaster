#!/bin/bash
# Exit on error
set -o errexit

# Convert static asset files
python manage.py collectstatic --no-input

# Generate migrations for main
python manage.py makemigrations main 

# Apply any outstanding database migrations
python manage.py migrate

# Start the application using Gunicorn
python -m gunicorn platemaster.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000