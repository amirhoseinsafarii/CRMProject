from django.urls import path

from . import views

app_name = 'followup'
urlpatterns = [
    path('send_email/<int:pk>/', views.email, name="email"),
    path('create-followup/', views.FollowUpCreate.as_view(), name='create-followup'),
    path('list-followup/', views.FollowUpList.as_view(), name='list-followup'),
]