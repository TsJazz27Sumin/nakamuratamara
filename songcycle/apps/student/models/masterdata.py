from django.db import models
from django.utils import timezone

class MasterData(models.Model):

    code = models.CharField(default="000", max_length=3)
    sub_code = models.CharField(default="00", max_length=2)
    value = models.CharField(default="nothing", max_length=50)
    sub_value = models.CharField(default="nothing", max_length=50)
    comment = models.CharField(default="", max_length=50)
