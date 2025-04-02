web: python3 manage.py migrate && python3 manage.py collectstatic --noinput && gunicorn appointment_crm.wsgi:application --bind 0.0.0.0:$PORT
