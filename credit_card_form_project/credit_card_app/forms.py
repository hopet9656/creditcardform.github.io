from django import forms
from .models import CreditCard

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['cardholder_name', 'card_number', 'expiration_date', 'cvv']
