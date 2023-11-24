from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def registration_mail(mail):
    send_mail('Registration', 'You successfully registered on the site', settings.EMAIL_HOST_USER,
              [mail], fail_silently=False)
