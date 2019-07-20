from django import forms


class PagingForm(forms.Form):

    previous = forms.BooleanField(required=False, initial=False)
    next = forms.BooleanField(required=False, initial=False)
    target_page = forms.IntegerField(required=False, initial=1)
    current_page = forms.IntegerField(required=True)
