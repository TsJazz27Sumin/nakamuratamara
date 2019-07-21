from django import forms


class UserSearchForm(forms.Form):

    email = forms.CharField(required=False, max_length=256)
    full_name = forms.CharField(required=False, max_length=200)
