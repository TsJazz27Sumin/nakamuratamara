from django.db import models


class MasterData(models.Model):

    class Meta:
        app_label = 'student'

    code = models.CharField(default="000", max_length=3)
    sub_code = models.CharField(default="00", max_length=2)
    value = models.CharField(default="nothing", max_length=100)
    sub_value = models.CharField(default="nothing", max_length=100)
    comment = models.CharField(default="", max_length=100)
