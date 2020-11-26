from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        fields = ['name','email','subject','message']
        model= Contact
