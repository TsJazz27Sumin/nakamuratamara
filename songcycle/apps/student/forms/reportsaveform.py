from django import forms
from django.core.files.storage import default_storage
from datetime import datetime

class ReportSaveForm(forms.Form):

    file_name = forms.CharField(required=True, max_length=100)
    file_path = forms.CharField(required=True, max_length=100)
    auther_user_id = forms.CharField(required=True, max_length=5)
    comment = forms.CharField(required=False, max_length=100)
