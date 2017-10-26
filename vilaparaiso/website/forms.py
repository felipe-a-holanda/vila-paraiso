from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ja cadastrado")
        return email
