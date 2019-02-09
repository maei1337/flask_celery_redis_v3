FROM python:3.6-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
