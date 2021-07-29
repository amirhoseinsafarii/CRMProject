from django import forms


class LoginForm(forms.Form):
    """
        login form
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)