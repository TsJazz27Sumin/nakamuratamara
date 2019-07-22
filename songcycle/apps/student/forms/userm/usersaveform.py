from django import forms


class UserSaveForm(forms.Form):

    user_id = forms.CharField(required=False, max_length=5)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=200)
    last_name = forms.CharField(required=True, max_length=200)
    authority = forms.CharField(required=True, max_length=2)
    status = forms.CharField(required=True, max_length=2)
    comment = forms.CharField(required=False, max_length=100)
