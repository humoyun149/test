from celery import shared_task
from django.core.mail import send_mail

from root import settings


@shared_task
def send_to_user_email(email: str, message: str):
    send_mail('Tema', message, settings.EMAIL_HOST_USER, [email])
    return f'{email} ga yuborildi'
