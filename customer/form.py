from django import forms
from .models import Customer, Contact

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model= Customer
        fields = ['name', 'address', 'phone', 'checked', 'contract']
        widgets = {
            'contract': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ['name', 'title', 'email', 'phone']