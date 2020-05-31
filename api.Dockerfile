FROM python:3.7-alpine

ENV GUNICORN_WORKERS 5
ENV GUNICORN_HOST 0.0.0.0


EXPOSE 8000

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD gunicorn -b $GUNICORN_HOST:8000 -w $GUNICORN_WORKERS api:app
