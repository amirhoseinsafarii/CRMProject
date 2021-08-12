from django.conf.urls import include
from django.urls import path
from organization.serializers import OrganizationSerializer
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('organization', views.OrganizationViewSet)

app_name = 'organization'
urlpatterns = [
    path('', views.Home_page, name='home-page'),
    path('create-org/', views.CreateOrganization.as_view(), name='create-org'),
    path('organization-list', views.ListOrganization.as_view(), name='list-organization'),
    path('view-Organization/<int:pk>', views.ViewOrganization.as_view(), name='vieworganization'),
    path('edit-organization/<int:pk>', views.EditOrganization.as_view(), name='edit'),
    path('api/v1/', include(router.urls), name='organization-list-api')
]