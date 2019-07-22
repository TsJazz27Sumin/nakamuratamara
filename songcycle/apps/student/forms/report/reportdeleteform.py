from django import forms


class ReportDeleteForm(forms.Form):

    report_id = forms.CharField(required=True, max_length=7)
    current_page = forms.IntegerField(required=True)
