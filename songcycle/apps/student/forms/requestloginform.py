from django import forms

class RequestLoginForm(forms.Form):
    
    email = forms.EmailField()