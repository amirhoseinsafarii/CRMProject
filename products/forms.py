from django import forms
from . import models


class CalcForm(forms.Form):
    """
    Form for calculator
    """
    pass


class PostForm(forms.ModelForm):
    """
    Model form for Post model
    """

    class Meta:
        model = models.Product
        fields = [
            'name',
            'price',
            'image',
        ]
