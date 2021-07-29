from django.urls import path

from . import views

app_name = 'organization'
urlpatterns = [
    path('create-org/', views.CreateOrganization.as_view(), name='create-org'),
    path('organization-list', views.ListOrganization.as_view(), name='list-organization'),
    path('view-Organization/<int:pk>', views.ViewOrganization.as_view(), name='vieworganization'),
    path('edit-organization/<int:pk>', views.EditOrganization.as_view(), name='edit'),
]