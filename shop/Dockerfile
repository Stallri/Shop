FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

WORKDIR /app

RUN mkdir /app/static
RUN mkdir /app/media

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input\
    && gunicorn shop.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000