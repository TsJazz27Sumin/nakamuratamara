from django import forms


class ReportSaveForm(forms.Form):

    file_name = forms.CharField(required=True, max_length=100)
    file_path = forms.CharField(required=True, max_length=100)
    auther_user_id = forms.CharField(required=True, max_length=5)
    target_year = forms.CharField(required=True, max_length=4)
    comment = forms.CharField(required=False, max_length=100)
