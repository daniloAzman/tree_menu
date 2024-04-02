#!/bin/bash

if [ "$DEBUG"==True ]; then
    python manage.py load_data
fi

gunicorn app.wsgi:application --bind 0:8000