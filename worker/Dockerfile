FROM python:3.6-slim
RUN mkdir worker
COPY . /worker
WORKDIR /worker
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT celery -A tasks worker --loglevel=info
