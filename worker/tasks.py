from celery import Celery
import time

celery = Celery(
                'tasks',
                broker='redis://redis:6379',
                backend='redis://redis:6379'
)

@celery.task(name='mytasks.add')
def add(zahl, b):
    time.sleep(5)
    return zahl + b
