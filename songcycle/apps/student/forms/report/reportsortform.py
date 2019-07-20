from django import forms

class ReportSortForm(forms.Form):

    target_sort_item = forms.CharField(required=True)
    target_descending_order = forms.BooleanField(required=True)
