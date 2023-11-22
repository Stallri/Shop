FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN adduser --disabled-password test_user-user
USER test_user-user
CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000

EXPOSE 8000