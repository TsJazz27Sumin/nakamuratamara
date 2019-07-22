from django import forms


class UserDeleteForm(forms.Form):

    user_id = forms.CharField(required=True, max_length=5)
    current_page = forms.IntegerField(required=True)
