from django.db import models
from django.utils import timezone

class DownloadInformation(models.Model):

    class Meta:
        app_label = 'student'

    report_id = models.CharField(max_length=7)
    user_id = models.CharField(max_length=5)
    download_timestamp = models.DateTimeField (default=timezone.now)

