from django import forms
from django.core.files.storage import default_storage
from datetime import datetime

class PagingForm(forms.Form):

    previous = forms.BooleanField(required=False, initial=False)
    next = forms.BooleanField(required=False, initial=False)
    target_page = forms.IntegerField(required=False, initial=1)
    current_page = forms.IntegerField(required=True)
