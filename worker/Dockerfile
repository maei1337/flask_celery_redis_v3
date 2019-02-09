FROM python:3.6-slim
RUN mkdir /worker
WORKDIR /worker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT celery -A tasks worker --loglevel=info
