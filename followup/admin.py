from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.FollowUP)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = (
       'content',
       'organization',
    )

@admin.register(models.EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'sender', 
        'receiver', 
        'status'
        ]
    list_filter = [
        'status', 
        'receiver'
        ]
