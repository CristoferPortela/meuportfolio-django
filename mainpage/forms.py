from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact 
        fields = ('name', 'email', 'subject', 'message')

        labels = {
            'name': '',
            'email' : '',
            'subject':  '',
            'message': '',
        }

        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'Your Name...'}), 
            'email' : forms.TextInput(attrs = {'placeholder': 'Your Email...'}),
            'subject': forms.TextInput(attrs = {'placeholder': 'Subject...'}), 
            'message': forms.TextInput(attrs = {'placeholder': 'Message...'}),
        }