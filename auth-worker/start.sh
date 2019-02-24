#!/bin/sh -e
exec gunicorn -b 0.0.0.0:8080 --name app --reload code.app:app &
celery worker --app=code.tasks.celery --hostname=code.${TASK_QUEUE}@%h --queues=${TASK_QUEUE} --uid=823 --loglevel=INFO
