web: gunicorn task_manager.wsgi --log-file -
release: python manage.py migrate
release: python manage.py makemigrations