import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

BROKER_URL=os.environ.get('BROKER_URL')
CELERY_RESULT_BACKEND=os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ROUTES = {
   'task_serializer': 'json',
   'result_serializer': 'json',
   'accept_content': ['json']
}
