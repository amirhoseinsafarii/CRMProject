from django.contrib import admin

from . import models

@admin.register(models.OrganizationProducts)
class OrganizationProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'products_s',
    )
    list_filter = (
        's_products',
    )
    search_fields = (
        'name__icontains',
    )


@admin.action(description='t')
def is_Includesـtaxes(modeladmin, request, queryset):
    queryset.update(is_Includesـtaxes=True)


# disable tax
@admin.action(description='f')
def is_not_Includesـtaxes(modeladmin, request, queryset):
    queryset.update(is_Includesـtaxes=False)

@admin.register(models.Product)
class ProductsAdmin(admin.ModelAdmin):
   
    list_display = (
        'name',
        'price',
        'image',
        'is_Includesـtaxes',
        'description',
    )
    search_fields = (
        'name__icontains',
    )
    list_filter = (
        'is_Includesـtaxes',
    )
    actions = [
        is_Includesـtaxes,
        is_not_Includesـtaxes,
    ]