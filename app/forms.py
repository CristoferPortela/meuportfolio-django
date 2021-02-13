"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class AuthForm(AuthenticationForm):
    """Authentication form which uses bulma CSS."""
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'input',
                'placeholder': 'User name'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            {
                'class': 'input',
                'placeholder':'Password'
            }
        )
    )
