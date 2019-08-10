from django import forms


class TargetYearForm(forms.Form):

    target_year = forms.IntegerField(required=True)
