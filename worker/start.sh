#!/bin/sh -e
exec gunicorn -b 0.0.0.0:8080 --name app --reload worker.tasks:app &
celery worker --app=worker.tasks.celery --hostname=worker.${TASK_QUEUE}@%h --queues=${TASK_QUEUE} --uid=823 --loglevel=INFO
