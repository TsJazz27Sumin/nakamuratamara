from django import forms


class SortForm(forms.Form):

    target_sort_item = forms.CharField(required=True)
    target_descending_order = forms.CharField(required=True)
