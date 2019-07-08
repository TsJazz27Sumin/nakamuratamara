from django.db import models
from django.utils import timezone

class AccessInformation(models.Model):

    class Meta:
        app_label = 'student'
        
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

    