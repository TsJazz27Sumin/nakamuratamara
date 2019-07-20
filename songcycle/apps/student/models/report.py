from django.db import models
from django.utils import timezone


class Report(models.Model):

    class Meta:
        app_label = 'student'

    report_id = models.CharField(max_length=7, unique=True)
    auther_user_id = models.CharField(max_length=5)
    target_year = models.CharField(default="2019", max_length=4)
    file_name = models.CharField(max_length=100)
    google_file_id = models.CharField(default="", max_length=100)
    comment = models.CharField(default="", max_length=100)
    create_user_id = models.CharField(max_length=5)
    create_timestamp = models.DateTimeField(default=timezone.now)
    update_user_id = models.CharField(max_length=5)
    update_timestamp = models.DateTimeField(default=timezone.now)
