from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.FollowUP)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = (
       'title',
       'content',
       'organization',
    )
