from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_tasks(subject,site_name,email,message):
    print('working-----------')
    send_mail(
            subject,
            f'message from {site_name} \n email : {email} \n Message : {message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )