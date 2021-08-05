from . import models
from django import forms

class QuoteForm(forms.ModelForm):


    class Meta:
        model = models.Quote
        fields = [
            'organization',
            ]

class QuoteItemForm(forms.ModelForm):


    class Meta:
        model = models.QuoteItem
        fields = [
            'quote',
            'product', 
            'qty', 
            'discount', 
            ]