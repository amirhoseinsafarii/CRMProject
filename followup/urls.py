from django.urls import path

from . import views

app_name = 'followup'
urlpatterns = [
    path('send_email/<int:pk>/', views.email, name="email"),
    path('create-followup/<int:pk>/', views.FollowUpCreate.as_view(), name='create-followup'),
    path('list-followup/<int:pk>/', views.followup_list, name='list-followup'),
]