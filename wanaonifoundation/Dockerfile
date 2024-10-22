FROM python:3.11.9-slim
WORKDIR /app
COPY . /app
RUN pip install django channels channels_redis gunicorn
EXPOSE 8000
CMD ["gunicorn", "wanaonifoundation.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]

