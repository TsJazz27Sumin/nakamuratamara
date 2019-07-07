from django.db import models
from django.utils import timezone

class TemporarilyLoginUrl(models.Model):

    request_email = models.EmailField()
    onetime_password = models.CharField(max_length=200)
    send_email_date_timestamp = models.DateTimeField (default=timezone.now)
