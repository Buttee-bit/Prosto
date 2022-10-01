from email import message
from django import forms

class NameForm(forms.Form):
    message = forms.CharField(label='Your name', max_length=100)