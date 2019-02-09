from celery import Celery
import requests
import time
from flask import jsonify
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

celery = Celery(
                'tasks',
                broker='redis://redis:6379',
                backend='redis://redis:6379'
)

MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
FROM_TITLE = os.environ.get("FROM_TITLE")
FROM_EMAIL = os.environ.get("FROM_EMAIL")


@celery.task(name='mytasks.add')
def send_simple_message(msg, sub, email):
    time.sleep(5)
    res = requests.post(
		f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
		auth=("api", f"{MAILGUN_API_KEY}"),
		data={"from": f"{FROM_TITLE} <{FROM_EMAIL}>",
			"to": f"{email}",
			"subject": f"{sub}",
			"text": f"{msg}"})
