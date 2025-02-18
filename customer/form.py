from django.forms import ModelForm
from .models import Customer, Contact

class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields = ['name', 'address', 'phone', 'checked']


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields = ['name', 'title', 'email', 'phone']