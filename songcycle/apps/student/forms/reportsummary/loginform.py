from django import forms


class LoginForm(forms.Form):

    password = forms.CharField(required=True)
    targetyear = forms.IntegerField(required=True)
