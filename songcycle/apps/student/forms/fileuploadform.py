from django import forms
from django.core.files.storage import default_storage

class FileUploadForm(forms.Form):
    file_source = forms.FileField()

    def save(self):
        upload_file = self.cleaned_data['file_source']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name) ,file_name