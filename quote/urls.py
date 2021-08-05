from django.urls import path
from . import views

app_name = 'quote'
urlpatterns = [
    path('quote-create/', views.QuoteCreate.as_view(), name='quote-create'),
    path('quoteitem-create/<int:pk>/', views.QuoteItemCreate.as_view(), name='quoteitem-create'),
    path('quote-list/', views.QuoteList.as_view(), name='quote-list'),
    path('quote-print/<int:pk>/', views.QuotePrint.as_view(), name='print-quote'),
]