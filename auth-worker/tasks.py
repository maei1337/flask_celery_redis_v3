from celery import Celery
import time
import sys

sys.path.append('/code')

import celeryconfig
celery = Celery('tasks')

celery.config_from_object('celeryconfig')

@celery.task(name='mytasks.add')
def send_simple_message(zahl):
    time.sleep(5)
    result = zahl * zahl
    return result

@celery.task(name='mytasks.sub')
def sub(zahl):
    time.sleep(5)
    result = 999 * zahl
    return result
