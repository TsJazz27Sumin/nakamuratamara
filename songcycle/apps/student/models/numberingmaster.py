from django.db import models


class NumberingMaster(models.Model):

    class Meta:
        app_label = 'student'

    code = models.CharField(max_length=2)
    initial = models.CharField(max_length=1)
    value = models.IntegerField(default=0)
    comment = models.CharField(default="", max_length=100)
