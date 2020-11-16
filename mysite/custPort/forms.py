from django import forms

class SignIn(forms.Form):
    user_name = forms.CharField(initial = "User name")
    password = forms.CharField(widget=forms.PasswordInput)
    