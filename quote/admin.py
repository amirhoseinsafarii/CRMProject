from django.contrib import admin
from . import models


@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    """
        manage in admin
    """
    list_display = (
        'user',
    )

@admin.register(models.QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    """
        manage in admin
    """
    list_display = (
        'product',
        'pricee',
        'qty',
        'discount',
    )
