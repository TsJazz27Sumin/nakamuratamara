from django import forms


class ReportSearchForm(forms.Form):

    target_year = forms.CharField(required=False, max_length=4)
    full_name = forms.CharField(required=False, max_length=100)
    file_name = forms.CharField(required=False, max_length=100)
