web: gunicorn website.wsgi --log-file -

worker: celery -A website worker
beat: celery -A website beat -S django
