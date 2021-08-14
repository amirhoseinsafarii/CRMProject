from django.contrib import admin
from . import models

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
        manage in admin for organization
    """
    list_display = (
        'city',
        'organization_name',
        'phone',
        'number_of_labor',
        'organization_products',
        'full_name',
        'phone_number',
        'email',
    )
    search_fields = (
        'organization_name__icontains',
        'Manufactured_products__icontains',
    )
    list_filter = (
        'Manufactured_products',
    )