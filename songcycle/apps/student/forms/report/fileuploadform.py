from django import forms
from django.core.files.storage import default_storage
from datetime import datetime


class FileUploadForm(forms.Form):

    file_source = forms.FileField()

    def save(self):

        upload_file = self.cleaned_data['file_source']
        today = datetime.now().strftime("%Y/%m/%d/")

        # Herokuは、ローカルファイルシステムの変更はすべて削除されるので、一時ファイル扱い。
        file_name = default_storage.save(
            "uploads/" + today + upload_file.name, upload_file)

        return default_storage.url(file_name)
