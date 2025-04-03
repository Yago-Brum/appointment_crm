#!/bin/bash
python manage.py migrate
gunicorn appointment_crm.wsgi:application