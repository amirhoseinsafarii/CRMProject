from . import models
from django import forms

class QuoteForm(forms.ModelForm):


    class Meta:
        model = models.Quote
        fields = [
            'slug',
            ]

class QuoteItemForm(forms.ModelForm):


    class Meta:
        model = models.QuoteItem
        fields = [
            'product', 
            'qty', 
            'discount', 
            ]
