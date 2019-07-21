from django import forms


class ReportSearchSpForm(forms.Form):

    search_value = forms.CharField(required=False, max_length=100)
