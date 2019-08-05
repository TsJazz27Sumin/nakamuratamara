from django import forms


class LoginForm(forms.Form):

    password = forms.CharField(required=True, max_length=4)
