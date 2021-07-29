from django.contrib import admin
from . import models

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
        manage in admin
    """
    list_display = (
        'city',
        'organization_name',
        'phone',
        'number_of_labor',
        'org_product',
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