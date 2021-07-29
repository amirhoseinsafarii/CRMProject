from django.urls import path

from . import views

app_name = 'followup'
urlpatterns = [
    path('create-followup/', views.FollowUpCreate.as_view(), name='create-followup'),
    path('list-followup/', views.ListFollowUp.as_view(), name='list-followup'),
]