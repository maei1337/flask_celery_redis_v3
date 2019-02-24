FROM python:3.6-slim

RUN mkdir /worker
COPY requirements.txt /worker/
RUN pip install --no-cache-dir -r /worker/requirements.txt
RUN pip install gunicorn 

COPY . /worker/
RUN chmod +x /worker/start.sh


RUN useradd -u 823 -N -M --system -s /bin/bash celery
RUN addgroup celery
RUN adduser celery celery

CMD ["/worker/start.sh"]
