from django import forms

class createAccountForm(forms.Form):
    fname = forms.CharField(help_text="Enter first name.", required=True)
    lname = forms.CharField(help_text="Enter last name.", required=True)
    username = forms.CharField(help_text="Enter username.", required=True)
    password = forms.CharField(help_text="Enter password.", required=True)
