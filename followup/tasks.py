from . import models
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from organization.models import Organization
from . import enums
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags

@shared_task(serializer='json')
def send_email_task(body,receiver, sender):
    try:
        send_mail('پیش فاکتور',
                  strip_tags(body),
                  settings.EMAIL_HOST_USER,
                  [receiver],
                  html_message=body,
                )
        models.EmailHistory.objects.create(receiver=Organization.objects.get(email=receiver),status=enums.EmailStatus.SENT,sender=get_user_model().objects.get(username=sender))
        #models.EmailHistory.objects.create(sender=sender,receiver=Organization.objects.get(email=receiver),status=enums.EmailStatus.SENT)
        return 'Email Send Successfully'
    except:
        models.EmailHistory.objects.create(receiver=Organization.objects.get(email=receiver),status=enums.EmailStatus.FAILED,sender=get_user_model().objects.get(username=sender))
        #models.EmailHistory.objects.create(sender=sender,receiver=receiver,status=enums.EmailStatus.FAILED)
        return 'Email not Send'
