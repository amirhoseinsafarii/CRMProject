from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/user/', views.UserAPIView.as_view(), name='user'),
]