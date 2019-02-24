FROM python:3.6-slim
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install gunicorn

COPY . /code/
RUN chmod +x /code/start.sh

RUN useradd -u 823 -N -M --system -s /bin/bash celery
RUN addgroup celery
RUN adduser celery celery

RUN mkdir -p /var/run/celery
RUN mkdir -p /var/log/celery
RUN chown -R celery:celery /var/run/celery
RUN chown -R celery:celery /var/log/celery

COPY celeryd /etc/init.d/celeryd
RUN chown -R root:root /etc/init.d/celeryd

COPY celeryd.conf /etc/default/celeryd
RUN chmod 640 /etc/default/celeryd

CMD ["/code/start.sh"]
