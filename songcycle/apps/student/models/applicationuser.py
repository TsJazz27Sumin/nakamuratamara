from django.db import models
from django.utils import timezone

class ApplicationUser(models.Model):

    class Meta:
        app_label = 'student'

    user_id = models.CharField(max_length=5, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(default="nothing", max_length=100)
    last_name = models.CharField(default="nothing", max_length=100)
    full_name = models.CharField(default="nothing", max_length=200)
    authority = models.CharField(default="00102", max_length=20)
    active = models.CharField(default="00", max_length=2)
    first_login_date_timestamp = models.DateTimeField (default=timezone.now)
    last_login_date_timestamp = models.DateTimeField (default=timezone.now)
    login_count = models.IntegerField (default=0)
    comment = models.CharField(default="", max_length=100)
    create_user_id = models.CharField(max_length=5)
    create_timestamp = models.DateTimeField (default=timezone.now)
    update_user_id = models.CharField(max_length=5)
    update_timestamp = models.DateTimeField (default=timezone.now)
