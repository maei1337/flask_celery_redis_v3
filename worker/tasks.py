from flask import Flask
from celery import Celery
import time
import sys

app = Flask(__name__)

sys.path.append('/worker')

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

if __name__ == '__main__':
    app.run()
