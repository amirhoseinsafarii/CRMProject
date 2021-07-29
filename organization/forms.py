from django import forms
from . import models


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = models.Organization
        fields = (
            'city',
            'organization_name',
            'phone',
            'number_of_labor',
            'full_name',
            'Manufactured_products',
            'phone_number',
            'email',
        )