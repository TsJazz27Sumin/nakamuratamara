from django import forms


class UserIdForm(forms.Form):

    user_id = forms.CharField(required=True, max_length=5)
