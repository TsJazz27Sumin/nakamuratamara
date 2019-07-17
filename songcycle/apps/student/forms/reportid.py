from django import forms
from django.core.files.storage import default_storage
from datetime import datetime

class ReportIdForm(forms.Form):

    report_id = forms.CharField(required=True, max_length=7)
