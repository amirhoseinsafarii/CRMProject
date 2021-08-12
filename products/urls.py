
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('products-list/', views.ListProduct.as_view(), name='list'),
]