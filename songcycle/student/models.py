from django.db import models
from django.utils import timezone

class Report(models.Model):
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    comment = models.TextField()
    attach = models.FileField(
        upload_to='uploads/%Y/%m/',
        verbose_name='添付ファイル'
    )
    create_date = models.DateTimeField(default=timezone.now)
    create_user = models.CharField(max_length=200)
    update_date = models.DateTimeField(default=timezone.now)
    update_user = models.CharField(max_length=200)

    def create(self):
        self.create_date = timezone.now()
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title