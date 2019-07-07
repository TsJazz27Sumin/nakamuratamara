from django.db import models
from django.utils import timezone

class AccessInformation(models.Model):

    event_type = models.CharField(default="", max_length=50)
    http_accept_language = models.CharField(default="", max_length=50)
    browser = models.CharField(default="", max_length=20)
    browser_version = models.CharField(default="", max_length=20)
    os = models.CharField(default="", max_length=20)
    os_version = models.CharField(default="", max_length=20)
    device = models.CharField(default="", max_length=20)
    device_brand = models.CharField(default="", max_length=20)
    device_type = models.CharField(default="", max_length=20)
    remote_addr = models.CharField(default="", max_length=50)
    access_date = models.DateField (default=timezone.now)
    access_date_timestamp = models.DateTimeField (default=timezone.now)
    success_value = models.CharField(default="", max_length=50)
    fault_value = models.CharField(default="", max_length=50)
    comment = models.CharField(default="", max_length=50)

class TemporarilyLoginUrl(models.Model):

    request_email = models.EmailField()
    onetime_password = models.CharField(max_length=200)
    send_email_date_timestamp = models.DateTimeField (default=timezone.now)

class ApplicationUser(models.Model):

    email = models.EmailField(unique=True)
    first_name = models.CharField(default="nothing", max_length=100)
    last_name = models.CharField(default="nothing", max_length=100)
    authority = models.CharField(default="00102", max_length=20)
    active = models.CharField(default="00", max_length=2)
    first_login_date_timestamp = models.DateTimeField (default=timezone.now)
    last_login_date_timestamp = models.DateTimeField (default=timezone.now)
    login_count = models.IntegerField (default=0)
    comment = models.CharField(default="", max_length=100)

class MasterData(models.Model):

    code = models.CharField(default="000", max_length=3)
    sub_code = models.CharField(default="00", max_length=2)
    value = models.CharField(default="nothing", max_length=50)
    sub_value = models.CharField(default="nothing", max_length=50)
    comment = models.CharField(default="", max_length=50)
