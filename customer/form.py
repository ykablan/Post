from django import forms
from .models import Customer, Contact


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model= Customer
        fields = ['name', 'address', 'phone', 'checked', 'contract']
        
 
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ['name', 'title', 'email', 'phone']